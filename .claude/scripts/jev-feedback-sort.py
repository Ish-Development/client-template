#!/usr/bin/env python3
"""Jev feedback sorter, for the client-feedback skill (step 2: sort each point to its step).

  python3 .claude/scripts/jev-feedback-sort.py points.txt     (one feedback point per line, client's exact words)

The steps and files come from the table in .claude/skills/client-feedback/SKILL.md, read on every run.
One Choice per point, all in one request. Below MIN_CONFIDENCE the point is marked "ask": Claude
asks the user where it belongs instead of guessing. Jev only routes; the client's words stay as they are.
"""
import os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "hooks"))  # jev.py lives with the hooks
from jev import key, ask, choice, read

MIN_CONFIDENCE = 0.5


def steps():
    md = read(".claude/skills/client-feedback/SKILL.md")
    rows = re.findall(r"^\| (?!The point|---)(.+?) \| (.+?) \| (.+?) \|$", md, re.M)
    return {f"s{i}": {"about": a, "step": s, "file": f} for i, (a, s, f) in enumerate(rows)}


def main():
    points = [l.strip().strip("-• ") for l in open(sys.argv[1]) if l.strip()] if len(sys.argv) > 1 else []
    if not points:
        sys.exit(__doc__)
    opts = steps()
    criteria = {sid: {"the_point_is_about": o["about"], "step": o["step"]} for sid, o in opts.items()}
    qs = {f"p{i}": choice({"point": p, "question": "What is `point` about?"}, criteria) for i, p in enumerate(points)}
    ans = ask(key(), {"feedback_points": points}, qs)
    print("| # | Point (client's words) | Step | File | Sure? |\n|---|---|---|---|---|")
    for i, p in enumerate(points):
        a = ans[f"p{i}"]; o = opts[a["choice"]]
        sure = f"{a['confidence']:.2f}" if a["confidence"] >= MIN_CONFIDENCE else f"ask ({a['confidence']:.2f})"
        print(f"| {i + 1} | {p} | {o['step']} | {o['file']} | {sure} |")


if __name__ == "__main__":
    main()
