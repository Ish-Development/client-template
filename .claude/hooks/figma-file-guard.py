#!/usr/bin/env python3
"""Figma file guard (PreToolUse hook on use_figma).

use_figma can change any Figma file Claude can reach. Before it runs, this checks the file is the
project's internal file: the "Internal, where we work" link in DESIGNERS.md. Another file, or no link
yet, and the user is asked first. Reading tools (screenshots, metadata) are not checked.

By hand: echo '{"tool_input": {"fileKey": "abc"}}' | python3 .claude/hooks/figma-file-guard.py
"""
import json, os, re, sys

ROOT = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def internal_key():
    """The file key in DESIGNERS.md's "Internal, where we work" link, or None while it is still blank."""
    try:
        md = open(os.path.join(ROOT, "DESIGNERS.md")).read()
    except OSError:
        return None
    m = re.search(r"Internal, where we work: \[[^\]]*\]\(https://www\.figma\.com/(?:design|file)/([0-9a-zA-Z]+)", md)
    return m.group(1) if m else None


def ask(reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                             "permissionDecision": "ask", "permissionDecisionReason": reason}}))


def main():
    try:
        key = (json.load(sys.stdin).get("tool_input") or {}).get("fileKey") or ""
    except ValueError:
        return
    ours = internal_key()
    if not ours:
        ask("DESIGNERS.md has no link to this project's internal Figma file yet. Ask the user for it "
            "(kickoff, Figma step) before changing anything in Figma.")
    elif key != ours:
        ask(f"This Figma file ({key}) is not this project's internal file ({ours}, DESIGNERS.md). "
            "Check with the user that this is the right file.")


if __name__ == "__main__":
    main()
