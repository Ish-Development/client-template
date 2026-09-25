---
name: copy-brief
description: When the client writes their own copy, make a Google Doc for every page with guidance for every section, linked from the sitemap and wireframe. Use when the user says "copy brief", "client writes the copy", or "make the copy docs".
---

# Copy brief for the client

Load the copy_client_brief files from agent/retrieval-rules.yaml first.
Needs a site plan (agent/site-plan.yaml). If it is empty, say so and stop.
Needs the Google Drive connector. If it is not connected, tell the user in plain words:
"Connect Google Drive in Claude's settings (Connectors), then ask me again."

## Guidance per section
For every section of every page, write short guidance for the client:
- What this section is for: its job (agent/site-jobs.md) in one line.
- What to write: the buyer question it answers (agent/journey.yaml), the objection it
  handles (agent/buying-committee.yaml), the proof it needs.
- Limits: word counts from constraints-messaging.yaml.
- For the section with the page's button: the button text is the page's next action.
Plain words. No jargon like "Informer" or "Converter" in the client's docs.

## Google Docs: one per page
1. Create a folder in the user's Google Drive: "CLIENT_NAME website copy".
2. For each page in site-plan.yaml, in order, create one Google Doc in that folder,
   named "NN Page name" (01 Home, 02 Product, ...). Upload it as HTML so it becomes a Doc:
   - Top: page name, what the page is for, the one thing a visitor should do next.
   - Then each section in order: the section name as a heading, the guidance in grey,
     and an empty box underneath titled "Write here".
3. Put each Doc's link in site-plan.yaml as copy_doc for that page.
4. Put the same guidance in each section's note in site-plan.yaml, then rebuild
   sitemap/index.html, so every page's wireframe shows it and links to its Doc.
5. Share nothing. Give the user the folder link. They decide who gets access.

## When the copy comes back
Read the Docs. Put each page's copy in copy/<page>/draft-version-one.md.
Offer a voice check (cw-voice-check) and a check against constraints-messaging.yaml.
Suggest changes. Never rewrite the client's copy silently.
