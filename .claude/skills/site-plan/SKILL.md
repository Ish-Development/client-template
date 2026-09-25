---
name: site-plan
description: Step 6. Plan the site by job and build the black and white HTML sitemap and wireframe for the client. Use when the user says "site plan", "site structure", "sitemap", or "information architecture".
---

# Site plan

Load the site_structure files from agent/retrieval-rules.yaml first.
If brand-positioning.yaml has no signed_off date, say so and ask whether to continue anyway.

## 1. Goal
Propose the site's one main goal (two at most), from the positioning and the workshop.
Something the business would celebrate: qualified leads or revenue. Ask the user to confirm.

## 2. Pages
Start from what the workshop settled (site-plan.yaml, status: hypothesis), then
research/07-site-implications.md (the current site: keep, fix, or drop each page),
and agent/journey.yaml (every stage needs pages that answer it).
For each page fill: id, name, url, parent, job, next_action, measured_by,
journey_stage, search_question, phase, sections.
- One job and one next action per page. Home may do several; name the main one.
- search_question comes from research/09-seo-aeo.md. Leave it empty rather than invent demand.
- Sections come from agent/section-library.md. A section can do a different job from its page.
- Group pages into nav_groups.
Show the draft as a simple list and ask for changes. Ask open choices one at a time.

## 3. Check
- Every journey stage has at least one page.
- All four jobs appear somewhere on the site, or the gap is named.
- Every page has one next action that leads toward a Converter.
- Every URL is unique and lowercase.
Report what fails.

## 4. Build the sitemap and wireframe
One deliverable: an overview tab with the whole information architecture, and one tab per
page with its wireframe (sections as grey boxes, in page order, sized s, m, or l).
1. Copy .claude/skills/site-plan/sitemap-template.html to sitemap/index.html.
2. Replace only the DATA block (window.SITE) with the site plan. Keep the rest unchanged.
3. Open sitemap/index.html with npx agent-browser, screenshot the overview and one page,
   and check the links work.
4. Tell the user: "The sitemap is ready: sitemap/index.html. Send it to the client for sign-off."
   When the user confirms sign-off, set signed_off in site-plan.yaml and status: validated.

## 5. Client writes the copy?
Check Copy in agent/research-brief.md. If the client writes the copy, say:
"The client writes the copy, so I'll make a Google Doc for every page, with guidance for
every section. OK?" On yes, use the copy-brief skill. It adds each Doc's link to the page
in site-plan.yaml and the sitemap, so the client clicks from the sitemap to the right Doc.

Offer to save to GitHub at the end.
