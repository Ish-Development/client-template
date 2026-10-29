#!/usr/bin/env python3
"""Jev task router (UserPromptSubmit hook).

Before Claude answers, Jev picks which task in CLAUDE.md ("Tasks, in workflow order") the user's
message is, and Claude gets a one-line pointer to that task's skill or files. The task list is read
from CLAUDE.md on every run, so editing CLAUDE.md updates the router. Low confidence or "none of
these": no pointer, Claude works as usual. Pattern: docs.typesafe.ai/cookbooks/skill_suggestion.

By hand: python3 .claude/hooks/jev-task-router.py "write copy for the home hero"
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jev import key, ask, choice, read

MIN_CONFIDENCE = 0.5  # tuned on test prompts; raise it if pointers show up for chat that isn't a task


def tasks():
    md = read("CLAUDE.md")
    block = md.split("Tasks, in workflow order", 1)[1].split("\n\n", 1)[0]
    items, cur = [], None
    for line in block.splitlines():
        if line.startswith("- "):
            cur = line[2:].strip(); items.append(cur)
        elif line.startswith("  ") and items:
            items[-1] += " " + line.strip()
    items = [t for t in items if ":" in t and not t.startswith("Every page")]
    items.append("save my work / save / commit: the Saving work steps in CLAUDE.md (show changes, ask, pull, commit, push)")
    return {f"t{i}": t for i, t in enumerate(items)}


def skill_description(task):
    """The 'Use when …' line of the task's skill, so Jev sees the same triggers the skill lists."""
    m = re.search(r"([\w-]+) skill", task)
    try:
        fm = read(f".claude/skills/{m.group(1)}/SKILL.md") if m else ""
    except OSError:
        return ""
    d = re.search(r"^description: (.*)$", fm, re.M)
    return d.group(1).strip() if d else ""


def route(prompt):
    k = key()
    if not k or prompt.strip().startswith("/") or len(prompt.split()) < 2:
        return None
    opts = tasks()
    criteria = {tid: {"task": t, "when": skill_description(t)} for tid, t in opts.items()}
    criteria["none"] = {"task": "None of these: a question, a quick fix, a follow-up or chat that is not one of the listed kit tasks"}
    q = choice({"message": prompt[:2000], "question": "Which kit task is `message` asking for?"}, criteria)
    a = ask(k, {"message": prompt[:2000]}, {"task": q}, timeout=10)["task"]
    if a["choice"] == "none" or a["confidence"] < MIN_CONFIDENCE:
        return None
    return opts[a["choice"]], a["confidence"]


def main():
    if len(sys.argv) > 1:
        r = route(" ".join(sys.argv[1:]))
        print(f"{r[1]:.2f}  {r[0]}" if r else "no pointer (none of the tasks, or not sure)")
        return
    try:
        prompt = json.load(sys.stdin).get("prompt", "")
        r = route(prompt)
    except Exception:
        return  # the router never gets in the way
    if r:
        task, conf = r
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext":
            f"Jev task router ({conf:.2f}): this looks like the CLAUDE.md task \"{task}\". If it is, follow that task "
            f"(its skill or retrieval-rules key) and load only its files. If it isn't, ignore this line."}}))


if __name__ == "__main__":
    main()
