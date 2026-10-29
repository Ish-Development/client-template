#!/usr/bin/env python3
"""Jev commit guard (PreToolUse hook on Bash).

CLAUDE.md: "The commit message is the decision and why, in plain words … If you don't know why, ask
before saving. Never invent the why." Before a `git commit` runs, Jev checks that the message names a
decision and gives a reason. If not, the commit is stopped and Claude is told to ask the user for the why.

By hand: python3 .claude/hooks/jev-commit-guard.py "Update VOICE.md"
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jev import key, ask, noul

MIN = 0.4  # below this for either question, the commit is stopped

QUESTIONS = {
    "decision": noul("Does the first line of `message` say what was decided or changed, in plain words?",
                     true="Names the change, e.g. 'Drop longevity from the copy', 'Rewrite the copy for every Phase 1 page'",
                     false="Only names a file or is vague, e.g. 'Update VOICE.md', 'changes', 'wip', 'fixes'"),
    "reason": noul("Does the first line of `message` give the reason for the change: a person's request, a problem it solves, or what it makes possible?",
                   true="Gives a why, e.g. '…: the client says it sounds like a supplement ad', '…, so no element is left empty or hidden'",
                   false="Only says what changed, with no reason, e.g. 'Update VOICE.md', 'Add hook script', 'Copy changes for Home'"),
}


def message_of(cmd):
    """The message of a real `git commit` in the command, or None. Text that only mentions
    git commit (a heredoc, an echo) doesn't count: the commit must start a command."""
    c = re.search(r"(?:^|&&|;|\|\||\n)\s*git\s+(?:-C\s+\S+\s+)?commit\b(.*)", cmd, re.S)
    if not c:
        return None
    rest = c.group(1)
    h = re.match(r"[^\n]*?-m\s+\"\$\(cat <<-?\s*'?(\w+)'?\n(.*?)\n\s*\1", rest, re.S)
    if h:
        return h.group(2).strip()
    m = re.match(r"[^\n]*?-m\s+(\"(?:[^\"\\]|\\.)*\"|'[^']*')", rest)
    return m.group(1)[1:-1].strip() if m else None


def check(msg):
    first = msg.strip().splitlines()[0]
    a = ask(key(), {"message": first}, QUESTIONS, timeout=10)
    return {q: a[q]["noul"] for q in QUESTIONS}


def main():
    if len(sys.argv) > 1:
        print(check(" ".join(sys.argv[1:])))
        return
    try:
        event = json.load(sys.stdin)
        msg = message_of((event.get("tool_input") or {}).get("command", ""))
        if not msg or not key():
            return
        p = check(msg)
    except Exception:
        return  # never block a commit because the check itself failed
    weak = [q for q in QUESTIONS if p[q] < MIN]
    if weak:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
            "permissionDecisionReason": (
                f"Jev commit guard: the message's first line doesn't clearly give the {' and the '.join(weak)} "
                f"({', '.join(f'{q} {p[q]:.2f}' for q in QUESTIONS)}). CLAUDE.md: the commit message is the decision and "
                "why, in plain words. Rewrite it; if you don't know why, ask the user. Never invent the why.")}}))


if __name__ == "__main__":
    main()
