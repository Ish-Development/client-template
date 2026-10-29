#!/usr/bin/env python3
"""Jev copy reviewer.

Runs after Claude writes or edits a copy draft (copy/<page>/draft-version-N.md) and sends the
findings back to Claude. Also runs by hand: python3 .claude/hooks/jev-copy-review.py <draft.md>

Countable rules (colons, banned words, word counts) stay in code. Judgment rules from
agent/VOICE.md and agent/constraints-messaging.yaml go to Jev (TypeSafe) as yes/no questions.
Jev's flags are evidence; VOICE.md wins (CLAUDE.md rule 6).

Needs JEV_API_KEY in .env. Without it, the hook does nothing.
"""
import json, os, re, sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jev import ROOT, key, noul, client_name, ask as jev_ask

CLIENT = client_name()

DRAFT = re.compile(r"^copy/(?!examples/)[^/]+/draft-version-\d+\.md$")


# ---------- Questions for Jev ----------
# Starting thresholds come from the first project that used this review; tune them on the client's own
# approved copy and on lines VOICE.md rejects.
# When the user approves a flagged line or rejects a passed one, tune the question or threshold here.

QUESTIONS = {
    "reader_not_you": (0.6, "calls the reader 'brands' / 'the client' instead of 'you' (VOICE.md Person)", noul(
        "Does `copy.text` refer to the reader as 'brands', 'the client' or 'customers' instead of addressing them as 'you'?")),
    "abstract_noun": (0.6, "abstract noun the buyer can't picture (VOICE.md Diction)", noul(
        "Does `copy.text` use an abstract noun a reader cannot picture, such as 'the standard', 'excellence', 'solutions', 'synergy' or 'value'?")),
    "punchline": (0.4, "punchline the buyer has to decode (constraints-messaging never_tone)", noul(
        "Does `copy.text` contain a clever or witty line that the reader has to decode to understand what the service does?")),
    "boast": (0.7, "claims we're better/faster/bigger, also inside a joke (constraints; VOICE.md lesson 'too cocky')", noul(
        f"Does `copy.text` claim or joke that {CLIENT} is better, faster, bigger, more reliable or more leading than its competitors, or that it gets things done remarkably fast?")),
    "staccato": (0.6, "three one-beat fragments in a row (VOICE.md Tics)", noul(
        "Does `copy.text` contain three or more very short fragments in a row, each without a verb, like 'One team. Four countries. Every visit on record.'?")),
    "contrast_formula": (0.6, "'not X but Y' / 'It's not about X' formula (VOICE.md Tics)", noul(
        "Does `copy.text` use a contrast formula such as 'not X but Y', 'It's not about X. It's about Y.' or 'X isn't Y, it's Z'?")),
    "no_verb": (0.7, "body without a subject and verb (VOICE.md lesson 2026-10-06, services cards)", noul(
        "Is `copy.text` only a noun phrase or list, with no sentence that has a subject and a main verb?")),
    "needs_source": (0.8, "states a fact to confirm: is it sourced or in 'To confirm'?", noul(
        f"Does `copy.text` state a specific fact about {CLIENT} that someone must confirm before publishing: a number, a customer name, a location, a time, or a service only some companies offer?")),
}
HEADING_QS = ["reader_not_you", "abstract_noun", "punchline", "boast", "contrast_formula"]


# ---------- Parse the draft into copy units ----------

COPY_LABELS = {"h1", "heading", "intro", "subhead", "eyebrow", "button", "buttons", "text", "body", "title", "quote", "link"}
HEADING_LABELS = {"h1", "heading", "title", "eyebrow"}
TABLE_COPY_COLS = {"title", "body", "text", "heading", "question", "answer", "quote", "subtitle", "intro"}
SKIP_LINE = re.compile(r"^\s*(-\s*)?(to confirm|sources?|changed|left out|date|out-of|note|why)\b", re.I)


def clean(t):
    t = re.sub(r"\s*\((?:[^()]|\([^()]*\))*\)", "", t)       # notes in brackets: (114), (S400; ...)
    t = re.sub(r"\s*\([^)]*$", "", t)                        # a note that runs onto the next line
    t = re.sub(r"\s*\[S\d+[^\]]*\]", "", t)                 # source tags
    return t.strip().strip("|").strip()


LABELLED = re.compile(r"^([A-Za-z][A-Za-z0-9 /]*?)(?:\s*\([^)]*\))?:\s*(.+)$")
SIBLING_LABELS = {"title", "text", "body"}


def labelled(part, section, units):
    """'Card 1 Title: …' / 'Text: …' / 'H1 (15 words): …' → a copy unit, if the label names copy."""
    lm = LABELLED.match(part.strip())
    if not lm:
        return False
    full = lm.group(1).strip()
    label = full.lower() if full.lower() in COPY_LABELS else full.lower().split()[-1]
    if label not in COPY_LABELS or not clean(lm.group(2)):
        return label in COPY_LABELS
    kind = "heading" if label in HEADING_LABELS else ("button" if label in {"button", "buttons", "link"} else "body")
    unit = {"section": section, "label": full, "kind": kind, "text": clean(lm.group(2))}
    if label in SIBLING_LABELS:  # numbered items and "Card N" lines in one section are siblings
        unit["group"], unit["label"] = section, label
    units.append(unit)
    return True


def parse(md):
    units, section, top, header, faq = [], "", "", None, None
    for raw in md.splitlines():
        line = raw.rstrip()
        if line.startswith("## "):
            top = section = line[3:].strip()
            header = faq = None
            continue
        if line.startswith("### "):
            section, header, faq = f"{top} / {line[4:].strip()}", None, None
            continue
        if not line.strip() or line.startswith("# ") or SKIP_LINE.match(line):
            header = None if not line.strip().startswith("|") else header
            if SKIP_LINE.match(line):
                faq = None
            continue
        if line.lstrip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if header is None:
                header = [re.sub(r"\s*\(.*\)", "", c).lower() for c in cells]
                table_id = f"{section}#{len(units)}"
                continue
            if set(line) <= set("|-: "):
                continue
            for col, cell in zip(header, cells):
                if col in TABLE_COPY_COLS and clean(cell):
                    kind = "heading" if col in {"title", "heading", "question"} else "body"
                    units.append({"section": section, "label": col, "kind": kind, "text": clean(cell), "group": table_id})
            continue
        header = None
        m = re.match(r"^(\d+)\.\s+(.*)", line)
        if m:
            faq = None
            if labelled(m.group(2), section, units):
                continue
            units.append({"section": section, "label": f"FAQ {m.group(1)} question", "kind": "heading", "text": clean(m.group(2))})
            faq = {"section": section, "label": f"FAQ {m.group(1)} answer", "kind": "body", "text": ""}
            units.append(faq)
            continue
        if faq is not None and raw.startswith(("   ", "\t")):
            faq["text"] = (faq["text"] + " " + clean(line)).strip()
            continue
        faq = None
        body = line.strip()[2:] if line.strip().startswith("- ") else line.strip()
        for part in body.split(" · "):
            labelled(part, section, units)
    return [u for u in units if u["text"]]


# ---------- Code checks ----------

def banned_words():
    words = ["leverage", "seamless", "robust", "unlock", "empower", "transformative", "pivotal", "comprehensive",
             "when it comes to", "at the end of the day"]
    try:
        voice = open(os.path.join(ROOT, "agent/VOICE.md")).read()
        block = voice.split("### Words we never use", 1)[1].split("###", 1)[0]
        for line in block.splitlines():
            if not line.startswith("- ") or "…" in line:
                continue
            head = line[2:].split(":", 1)[0]
            quoted = re.findall(r'"([^"]+)"', head)
            words += quoted if quoted else [head.strip()]
        tics = re.search(r"\| Words: ([^|]+)\|", voice)
        if tics:
            words += [w.strip().strip('"') for w in tics.group(1).split(",")]
    except (OSError, IndexError):
        pass
    return sorted({w.lower() for w in words if w and len(w) > 2})


def code_checks(units):
    out, banned = [], banned_words()
    for u in units:
        t = u["text"]
        for w in banned:
            if re.search(r"\b" + re.escape(w) + r"\b", t, re.I):
                out.append((u, f"banned word '{w}' (VOICE.md Words we never use)"))
        if u["kind"] == "heading" and ":" in t:
            out.append((u, "colon in a heading or title (VOICE.md lesson 2026-10-07)"))
        if u["kind"] == "heading" and u["label"].lower() in {"h1", "heading"} and len(t.split()) > 10:
            out.append((u, f"heading has {len(t.split())} words; headings run 6–8 (VOICE.md Syntax)"))
        if re.search(r"\bNo \w[^.]*\.\s+No \w[^.]*\.\s+Just\b", t):
            out.append((u, "'No X. No Y. Just Z.' (VOICE.md Tics)"))
    page = " ".join(u["text"] for u in units)
    if len(re.findall(r"\bwithout\b", page, re.I)) > 1:
        out.append(({"section": "whole page", "label": "", "text": ""}, "'without' used more than once on the page (VOICE.md Tics)"))
    groups = {}
    for u in units:
        if u.get("group"):
            groups.setdefault((u["group"], u["label"]), []).append(u)
    for (_, label), us in groups.items():
        if len(us) < 2:
            continue
        words = [len(u["text"].split()) for u in us]
        limit = 4 if us[0]["kind"] == "heading" else 6
        if max(words) - min(words) > limit:
            out.append(({"section": us[0]["section"], "label": f"{label} column", "text": ""},
                        f"sibling {label} lengths run {min(words)}–{max(words)} words; keep within ±{limit // 2} (VOICE.md Syntax)"))
        firsts = [" ".join(u["text"].split()[:2]).lower() for u in us]
        dup = {f for f in firsts if firsts.count(f) >= 2}
        if dup and us[0]["kind"] == "body":
            out.append(({"section": us[0]["section"], "label": f"{label} column", "text": ""},
                        f"{len([f for f in firsts if f in dup])} cards open the same way ('{', '.join(sorted(dup))}…'); vary openings (VOICE.md lessons)"))
    return out


# ---------- Jev ----------

def ask(k, unit):
    qs = HEADING_QS if unit["kind"] == "heading" else list(QUESTIONS)
    if not unit.get("group"):  # the no-verb rule is for cards; a hero line may be a phrase (VOICE.md lesson 2026-10-06, hero)
        qs = [q for q in qs if q != "no_verb"]
    state = {"section": unit["section"], "copy": {"element": unit["label"], "text": unit["text"]}}
    answers = jev_ask(k, state, {q: QUESTIONS[q][2] for q in qs})
    return unit, {q: a["noul"] for q, a in answers.items()}


def jev_checks(k, units):
    flags, facts = [], []
    todo = [u for u in units if u["kind"] in ("heading", "body") and len(u["text"].split()) >= 2]
    with ThreadPoolExecutor(8) as pool:
        for unit, answers in pool.map(lambda u: ask(k, u), todo):
            for q, p in answers.items():
                threshold, why, _ = QUESTIONS[q]
                if p >= threshold:
                    (facts if q == "needs_source" else flags).append((unit, f"{why} [{q} {p:.2f}]"))
    return flags, facts, len(todo)


# ---------- Report ----------

def fmt(item):
    u, msg = item
    where = f"{u['section']} / {u['label']}".strip(" /")
    quote = f' "{u["text"][:90]}{"…" if len(u["text"]) > 90 else ""}"' if u.get("text") else ""
    return f"- {where}:{quote} → {msg}"


def review(path, k):
    units = parse(open(path).read())
    if not units:
        return None, None
    code = code_checks(units)
    flags, facts, n = jev_checks(k, units)
    rel = os.path.relpath(path, ROOT)
    lines = [f"Jev copy review of {rel} ({len(units)} elements, {n} sent to Jev)."]
    if code or flags:
        lines.append("Breaks a kit rule (fix it, or tell the user why it stays):")
        lines += [fmt(i) for i in code + flags]
    else:
        lines.append("No rule breaks found.")
    if facts:
        lines.append("Facts to check (each needs a source or a 'To confirm' line):")
        lines += [fmt(i) for i in facts]
    lines.append("Jev's flags are evidence, not rules: VOICE.md wins. A wrong flag is a reason to tune "
                 ".claude/hooks/jev-copy-review.py, not to change good copy.")
    short = f"Jev reviewed {rel}: {len(code) + len(flags)} rule flags, {len(facts)} facts to check."
    return "\n".join(lines), short


def main():
    if len(sys.argv) > 1:  # by hand
        k = key()
        if not k:
            sys.exit("No JEV_API_KEY in .env")
        text, _ = review(os.path.abspath(sys.argv[1]), k)
        print(text or "No copy found in that file.")
        return
    try:
        event = json.load(sys.stdin)
    except ValueError:
        return
    path = (event.get("tool_input") or {}).get("file_path") or ""
    rel = os.path.relpath(os.path.abspath(path), ROOT) if path else ""
    if not DRAFT.match(rel):
        return
    k = key()
    if not k:
        return
    try:
        text, short = review(os.path.join(ROOT, rel), k)
    except Exception as e:  # never break the edit; just say the review didn't run
        text, short = f"Jev copy review skipped for {rel}: {e}", f"Jev review skipped: {e}"
    if text:
        print(json.dumps({"systemMessage": short,
                          "hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": text}}))


if __name__ == "__main__":
    main()
