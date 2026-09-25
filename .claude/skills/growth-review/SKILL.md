---
name: growth-review
description: Step 10. Read the live site's data, compare each page with its job, find where visitors drop off, and recommend the next sprints. Use when the user says "growth review", "how is the site doing", "CRO", or "what should we build next quarter".
---

# Growth review

Load the growth_review files from agent/retrieval-rules.yaml first.

## Get the data
1. Webflow sites: use the Webflow connector, data_analyze_tool.
   - Site ID: "Built in" in agent/section-library.md. If missing, list sites and ask which one.
   - Window: the last full quarter, at most 100 days (the tool's limit).
   - Pull: traffic, top pages, traffic sources, top engagement events per page,
     and next-page flow for the key pages in agent/site-plan.yaml.
   - If Analyze is not switched on for the site, say so and stop the Webflow part.
2. Search Console: ask the user, in plain words:
   "Please export Search Console for the last 3 months: Performance, then the Pages
   tab and the Queries tab, Export as CSV. Drop the files in growth/data/ or paste them here."
   If they skip, mark Search Unknown.
3. Other sites (e.g. Astro): ask which analytics the site uses and how to get the data.
   Do not guess.

## Analyse
- For each page in agent/site-plan.yaml: visitors, how many took its next action, the rate.
  Use the engagement events that match the next action (the button or form).
- Find leaks: pages with many visitors and a low rate. Use next-page flow to see where people go.
- Compare with last quarter's report in growth/, if there is one.
- Re-ask the 5 answer engine questions from research/09-seo-aeo.md, one at a time in the chat,
  the same way as in research.

## Webflow Optimize tests
The connector cannot set up or read Optimize. Claude plans, the team runs it in Webflow.
1. Last quarter's tests: ask the user to paste each Optimize result (variants, visitors,
   next actions, winner). Record them in the report. Never guess a result.
2. New tests: pick 1-3 from the biggest leaks. For each one write:
   - the page and the section to test
   - what we think is wrong, based on the data
   - the variant copy, checked against agent/VOICE.md, agent/STYLE.md, and constraints-messaging.yaml
   - the measure: the page's next action from agent/site-plan.yaml
3. Personalisation ideas: where agent/buying-committee.yaml industry notes or traffic
   sources suggest different visitors need different copy.

1. Copy growth/report-template.md to growth/YYYY-QN.md and fill it in.
2. Recommend fixes ranked by impact. Tie each one to a finding and a sprint in agent/sprint-menu.md.
3. Only numbers from the data. Never invent benchmarks, conversion rates, or targets.
4. If the data contradicts research or /agent, flag it and add it to research/08-risks-and-questions.md.
5. Offer: "Want me to save this to GitHub?"
