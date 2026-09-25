---
name: copy
description: Step 8. Write copy for a part of the wireframe the user points at, with Compound Writing, and show it in the sitemap. Use when the user says "write copy for", "copy for the home hero", "write section 3 on the product page", or names a page or section from the sitemap.
---

# Copy

Only when we write the copy (agent/research-brief.md: Copy). If the client writes it,
use the copy-brief skill instead.

## 1. Find the part
The user points at a part of the wireframe in sitemap/index.html: a page and a section,
by name or number ("home, section 1", "the product hero", "all of the contact page").
Match it to agent/site-plan.yaml. If it is unclear, show the page's sections with their
numbers and ask which.

## 2. Brief for that part
Gather, for this section only:
- the page's job and next action, and the section's job and note (site-plan.yaml)
- the buyer role and their objections (buying-committee.yaml)
- the journey question (journey.yaml) and the search question (site-plan.yaml)
- proof we can use (brand-positioning.yaml proof_points, research/sources.md)
- limits (constraints-messaging.yaml)
Write it to copy/<page>/notes.md under the section's name.

## 3. Write
Use Compound Writing with agent/VOICE.md and agent/STYLE.md (see CLAUDE.md for where
its files live). Draft with cw-draft.
- A headline: write 3 options with cw-hook, each a different angle. The user picks.
- Only claims with a source or client confirmation. Never invent numbers, names, or quotes.
- If the section holds the page's button, the button text is the next action.

## 4. Check
Run cw-voice-check and cw-ai-check. Check constraints-messaging.yaml and the
ready-to-publish list in STYLE.md. Fix, then show the copy and what the checks found.

## 5. Save and show in the wireframe
- Write the copy to copy/<page>/draft-version-N.md under the section's name.
  New round, new version number. Never call a file final.
- Put the copy in the section's copy field in agent/site-plan.yaml.
- Rebuild sitemap/index.html so the wireframe box shows the copy.

## SEO and AEO, when a whole page is done
Write a page title (under 60 characters) and meta description (under 155) that answer
the page's search question. Check headings answer it too, and that key facts are
stated plainly enough for an AI answer to quote.

When the user corrects the copy, offer cw-save so the lesson becomes a rule.
