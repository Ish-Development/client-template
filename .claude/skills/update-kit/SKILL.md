---
name: update-kit
description: Bring the latest kit improvements from client-template into this client folder. Use when the user says "update the kit", "bring in the latest kit changes", or "get the template changes".
---

# Update kit

Brings improvements from Ish-Development/client-template into this client folder.
Never touches the client's own content.

## Before anything
If this folder is client-template itself, stop. Say: "This is the template. It is already the latest."

## Two kinds of files

Kit files: the method. Safe to replace with the template version.
- CLAUDE.md
- .claude/settings.json and everything in .claude/skills/
- agent/research-agent.md, agent/retrieval-rules.yaml, agent/site-jobs.md, agent/sprint-menu.md
- copy/README.md, copy/examples/README.md, growth/README.md, growth/report-template.md
- agent/visual/README.md, qa/README.md, human/visual-sources/README.md
- package.json, .gitignore, README.md
- examples/

Client files: filled in for this client. Never replace.
- Everything else in agent/, research/, and human/
- The Figma and Built links in agent/section-library.md

## Steps
1. Download the latest template to a temporary folder:
   gh repo clone Ish-Development/client-template "$(mktemp -d)/client-template" -- --depth 1
2. Compare each kit file with the template version. List the ones that differ, and in
   one line each, say what changed in plain words.
3. For client files, check if the template added new sections or fields (for example a
   new table in a research file). List them. These are added by hand, not replaced.
4. Show the list and ask: "Update these kit files?" Wait for a yes.
5. On yes: copy the kit files over. For new sections in client files, add them without
   changing anything already filled in.
6. If agent/retrieval-rules.yaml changed, check every file it lists exists. Report missing ones.
7. Say what was updated. Offer: "Want me to save this to GitHub?"
8. Delete the temporary folder.

If nothing differs, say: "This client already has the latest kit."
