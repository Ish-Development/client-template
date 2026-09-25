---
name: copy-brief
description: When the client writes their own copy, make a click-through wireframe and a Google Doc that tell them what to write in each section. Use when the user says "copy brief", "client writes the copy", or "make the copy doc".
---

# Copy brief for the client

Load the copy_client_brief files from agent/retrieval-rules.yaml first.

## Wireframe
1. Build a simple click-through HTML wireframe in copy/wireframe/: one HTML file per page
   in agent/site-plan.yaml, linked through a shared menu. Grey boxes, no design.
2. For each section on a page (from its sections list and section-library.md), show:
   - the section name and its job
   - what to write: the buyer question it answers (agent/journey.yaml), the objection it
     handles (agent/buying-committee.yaml), the proof it needs
   - limits: word counts from constraints-messaging.yaml
   - the page's one next action on its button
3. Open copy/wireframe/index.html in the browser to check the links work.

## Google Doc
1. Create one Google Doc in the user's Google Drive, named "CLIENT_NAME website copy".
   Same pages and sections as the wireframe, in order.
2. For each section: the guidance above in grey, then an empty space for the client.
3. Share nothing. Give the user the link and let them decide who gets access.

## When the copy comes back
Put it in copy/<page>/draft-version-one.md. Offer a voice check (cw-voice-check)
and a check against constraints-messaging.yaml. Suggest changes. Never rewrite silently.
