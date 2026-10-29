#!/usr/bin/env python3
"""Jev design check for one Figma page.

  python3 .claude/scripts/jev-design-check.py <page.json> --page home \
      [--library library.json] [--draft copy/home/draft-version-1.md]

page.json:    output of figma-read-page.js (sections, layouts, switches, visible text)
library.json: output of figma-read-library.js (layouts per component set)

What it checks:
- Plan coverage (Jev Choice): which Figma section does each section job in agent/site-plan.yaml? Gaps and order.
- Next action (Jev Noul): can the reader take the page's next_action from the page?
- Layout fit (Jev Choice): for each section, which layout in its set fits its job and content? A different
  confident pick is a design question for the designer, never a change (design-qa skill).
- Draft match (code): approved draft lines missing in Figma, Figma lines missing in the draft.
- Open items (code): [placeholders] and switches that are off, so each one is a known decision.
Jev's answers are evidence; the designer and agent/ files decide. Jev reads text only, not pixels.
"""
import argparse, importlib.util, json, os, re, sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "hooks"))  # jev.py lives with the hooks
from jev import ROOT, key, ask, noul, choice, read

SKIP_SECTIONS = re.compile(r"^(footer|nav|navbar|navigation)", re.I)


# ---------- agent/site-plan.yaml (no YAML library on every machine, so read it by pattern) ----------

def plan_for(page_id):
    text = read("agent/site-plan.yaml")
    m = re.search(rf"^  - id: {re.escape(page_id)}\n(.*?)(?=^  - id: |\Z)", text, re.M | re.S)
    if not m:
        sys.exit(f"No page '{page_id}' in agent/site-plan.yaml")
    block = m.group(1)
    field = lambda f: (re.search(rf"^    {f}: (.*)$", block, re.M) or [None, ""])[1].strip().strip("'\"")
    sec_block = block
    alias = re.search(r"sections: \*(\w+)", block)
    if alias:
        anchor = re.search(rf"sections: &{alias.group(1)}\n(.*?)(?=^  - id: |\Z)", text, re.M | re.S)
        sec_block = anchor.group(1) if anchor else ""
    sections = []
    for s in re.finditer(r"^\s+- name: (.+)\n((?:\s{8,}\w+:.*\n?)*)", sec_block, re.M):
        attrs = dict(re.findall(r"^\s+(\w+): (.*)$", s.group(2), re.M))
        sections.append({"name": s.group(1).strip(), "job": attrs.get("job", "").strip(),
                         "note": attrs.get("note", "").strip().strip("'\"")})
    return {"name": field("name"), "job": field("job"), "next_action": field("next_action"), "sections": sections}


# ---------- checks ----------

def summary(sec, limit=700):
    t = " / ".join(dict.fromkeys(sec["text"]))  # drop repeats (tab labels, duplicated pills)
    return t[:limit]


def coverage(k, plan, secs):
    state = {"figma_sections": {s["key"]: summary(s) for s in secs}, "next_action": plan["next_action"]}
    options = {s["key"]: f"The Figma section '{s['name']}' ({s.get('component') or 'frame'})" for s in secs}
    options["none"] = "No section on this page does this job"
    qs = {}
    for i, p in enumerate(plan["sections"]):
        qs[f"req_{i}"] = choice({"requirement": p, "question": "Which part of `figma_sections` does the job described in `requirement`?"}, options)
    for s in secs:
        qs[f"next_{s['key']}"] = noul(f"Does `figma_sections.{s['key']}` contain a button, link, phone number or email that lets the reader do `next_action`?")
    return ask(k, state, qs)


def layout_fit(k, sec, plan_sec, lib):
    state = {"section_job": plan_sec or {}, "component_set": {"name": lib["name"], "description": lib["description"]},
             "content": summary(sec, 900)}
    q = choice({"question": "Which layout of `component_set` fits `content` and `section_job` best?",
                "focus": "Judge how the content is shaped (how many items, steps, stories or people; text only or with images) against what each layout name says."},
               {l: {"layout": l, "what_it_is": lib["layoutDescriptions"][l]} for l in lib["layouts"]})
    return sec, ask(k, state, {"layout": q})["layout"]


def norm(t):
    return re.sub(r"[^a-z0-9%→]+", " ", t.lower()).strip()


def draft_match(draft_path, secs):
    spec = importlib.util.spec_from_file_location("review", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "hooks", "jev-copy-review.py"))
    review = importlib.util.module_from_spec(spec); spec.loader.exec_module(review)
    units = review.parse(open(draft_path).read())
    raw = open(draft_path).read()
    figma = {norm(t) for s in secs for t in s["text"]}
    draft = norm(raw)  # match against the whole draft, so lines in any draft format count
    missing = [u for u in units if norm(u["text"]) not in figma and len(u["text"].split()) >= 3
               and not re.search(r"\[[^\]]+\]", u["text"])]  # placeholders are listed under Open items
    extra = [(s["name"], t) for s in secs if not (s.get("component") or "").startswith("Contact / People")
             for t in dict.fromkeys(s["text"]) if len(t.split()) >= 6 and norm(t) not in draft and not re.search(r"\[.*\]", t)]
    return missing, extra


# ---------- report ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("figma"); ap.add_argument("--page", required=True)
    ap.add_argument("--library"); ap.add_argument("--draft")
    a = ap.parse_args()
    k = key()
    if not k:
        sys.exit("No JEV_API_KEY in .env")
    fig = json.load(open(a.figma))
    plan = plan_for(a.page)
    secs = [dict(s, key=f"s{i + 1}") for i, s in enumerate(fig["sections"]) if not SKIP_SECTIONS.match(s["name"])]
    by_key = {s["key"]: s for s in secs}
    out = [f"# Jev design check: {fig['frame']} (Figma {fig.get('id', '')})", "",
           f"Page plan: **{plan['name']}** ({plan['job']}), next action: \"{plan['next_action']}\".",
           "Jev reads the text and structure only, not the pixels. Every point is a question for the designer; "
           "Claude changes nothing in Figma without a yes (design-qa skill).", ""]

    ans = coverage(k, plan, secs)
    out += ["## Plan coverage (agent/site-plan.yaml)", "", "| Plan section | Job | Figma section | Sure? |", "|---|---|---|---|"]
    matched, gaps = [], []
    for i, p in enumerate(plan["sections"]):
        c = ans[f"req_{i}"]
        pick, conf = c["choice"], c["confidence"]
        name = by_key[pick]["name"] if pick in by_key else "**none**"
        sure = "yes" if conf >= 0.5 else f"unsure ({conf:.2f})"
        out.append(f"| {p['name']} | {p['job']} | {name} | {sure} |")
        if pick in by_key:
            matched.append((i, int(pick[1:]), p))
        if pick == "none" or conf < 0.3:
            gaps.append(p["name"])
    order = [f for _, f, _ in matched]
    out.append("")
    if gaps:
        out.append(f"- Missing or unclear on the page: {', '.join(gaps)}.")
    if order != sorted(order):
        out.append("- The Figma order differs from the plan order.")
    nexts = [(s["name"], ans[f"next_{s['key']}"]["noul"]) for s in secs]
    best = max(nexts, key=lambda x: x[1])
    out.append(f"- Next action: {'found in ' + best[0] if best[1] >= 0.7 else 'not clearly on the page'}"
               f" ({', '.join(f'{n} {p:.2f}' for n, p in nexts if p >= 0.5) or 'no section above 0.50'}).")

    plan_of = {f"s{f}": p for _, f, p in matched}
    if a.library:
        lib = {l["name"]: l for l in json.load(open(a.library))}
        cands = [(s, plan_of.get(s["key"]), lib[s["component"]]) for s in secs
                 if s.get("component") in lib and len(lib[s["component"]]["layouts"]) > 1]
        described = lambda l: all((l.get("layoutDescriptions") or {}).get(x) for x in l["layouts"])
        todo = [t for t in cands if described(t[2])]
        undescribed = sorted({t[2]["name"] for t in cands if not described(t[2])})
        out += ["", "## Layout fit (a design question when Jev confidently prefers another layout)", ""]
        if undescribed:
            out.append(f"- Not judged: {', '.join(undescribed)}. Their layouts have no description in Figma, and from names "
                       "alone Jev guesses (it read 'Side heading' as less of a steps layout than 'Steps'). A one-line "
                       "component description per layout, written or approved by the designer, turns this check on.")
        if todo:
            out += ["", "| Section | Set | Now | Jev's pick | Probability now / pick |", "|---|---|---|---|---|"]
        with ThreadPoolExecutor(6) as pool:
            for sec, c in pool.map(lambda t: layout_fit(k, *t), todo):
                now = (re.search(r"Type=([^,]+)", sec.get("variant") or "") or [None, "?"])[1]
                pick, probs = c["choice"], c["probabilities"]
                flag = " ← design question" if pick != now and probs.get(pick, 0) >= 0.5 and probs.get(now, 0) < 0.25 else ""
                out.append(f"| {sec['name']} | {sec['component']} | {now} | {pick}{flag} | {probs.get(now, 0):.2f} / {probs.get(pick, 0):.2f} |")

    if a.draft:
        missing, extra = draft_match(os.path.join(ROOT, a.draft) if not os.path.isabs(a.draft) else a.draft, secs)
        out += ["", f"## Figma against the draft ({a.draft})", ""]
        out += [f"- In the draft, not in Figma: \"{u['text'][:100]}\" ({u['section']})" for u in missing] or ["- Every draft line of 3+ words is in Figma."]
        out += [f"- In Figma, not in the draft: \"{t[:100]}\" ({n})" for n, t in extra]

    holes = [(s["name"], t) for s in secs for t in dict.fromkeys(s["text"]) if re.search(r"\[[^\]]+\]", t)]
    offs = [(s["name"], s["switchesOff"]) for s in secs if s.get("switchesOff")]
    out += ["", "## Open items", ""]
    out += [f"- Placeholder in {n}: \"{t}\"" for n, t in holes] or ["- No placeholders."]
    out += [f"- Switched off in {n}: {', '.join(o)} (a decision, never a way to fit copy: STYLE.md)" for n, o in offs]
    print("\n".join(out))


if __name__ == "__main__":
    main()
