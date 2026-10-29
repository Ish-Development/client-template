---
name: design-qa
description: Step 10. Critique the hi-fi design in Figma and QA the Webflow site. Claude builds nothing. Small Figma fixes only after the designer says yes. Webflow is read-only. Use when the user says "design critique", "check the design", "QA the site", or "internal QA".
---

# Design critique and internal QA

Claude does not design or build. It checks, reports, and fixes small things in Figma
only with the designer's yes. Load the design_qa files from agent/retrieval-rules.yaml.

## A. Figma design critique
1. Ask for the Figma link to the page or frames to check.
2. Read them with the Figma connector (design context, screenshots, variables).
   Then run the Jev design check: run .claude/scripts/figma-read-page.js in use_figma (set NODE_ID
   to the page frame) and .claude/scripts/figma-read-library.js, save both results as JSON, and run
   `python3 .claude/scripts/jev-design-check.py page.json --page <site-plan id> --library library.json
   --draft copy/<page>/draft-version-N.md`. It checks plan coverage and order, the next action, layout
   fit, Figma against the draft, placeholders and switched-off elements. Put its findings in the critique
   as design questions; Jev reads text, not pixels, and the designer decides. Layout fit only runs for
   sets whose layouts have a description in Figma (a gap the designer can close).
   Then run the Figma rules check: .claude/scripts/figma-rules-check.js in use_figma, ROOT_ID set to the page
   frame (copy rules) and to each component set the page uses (style rules). It lists every break of the rules
   in DESIGNERS.md with its layer. Hand-set values go under Small fixes; a rule broken across many sets (e.g.
   all borders) is one design question, not a list of fixes.
3. Check against the kit:
   - Visual system: colors, type, spacing, radius, effects match agent/visual/tokens.json.
     Flag values that are off-token or not bound to a variable.
   - Rules: Hard rules in the agent/visual/ topic files (logo, color, typography, imagery,
     layout, components, motion). Components match agent/visual/components.html.
   - Structure: the page has the sections from agent/site-plan.yaml, in order, and its
     one next action is visible.
   - Copy: the text matches the latest approved copy in copy/<page>/. Flag differences.
   - Consistency: the same component looks the same everywhere. Alignment, spacing rhythm.
   - Accessibility: text contrast, text size, tap target size.
4. Write the critique to qa/YYYY-MM-DD-figma-<page>.md, with a link to each frame:
   - Small fixes: off-token values, a missed border radius, spacing that breaks the scale,
     an unbound color. One line each: what it is, what it should be, where.
   - Design questions: anything bigger. Layout, hierarchy, imagery. Critique only, never fix.
5. Ask: "Should I fix the small ones in Figma? Check with the designer first if that is
   not you." Fix only what they approve, only small fixes, one by one, and report each.
   Never move, restyle, or restructure anything else.

## B. Webflow internal QA (read-only)
Never change anything in Webflow: no edits, no publishing, no form submissions.
1. Get the site from "Built in" in agent/section-library.md or ask for the staging URL.
2. Inspect with the Webflow connector (read only) and npx agent-browser on the staging URL.
3. Check:
   - Pages and URLs match agent/site-plan.yaml. Every page's next action is there and links
     to the right place.
   - Copy matches the approved copy in copy/<page>/.
   - Styles use the variables from agent/visual/tokens.json, not hard-coded values.
   - Screenshots at mobile (390px), tablet (768px), desktop (1440px). Spacing, radius,
     overflow, broken layouts.
   - Motion matches agent/visual/motion.json and agent/visual/motion.md.
   - Links: no broken links or 404s.
   - SEO: page title, meta description, one H1, alt text, per copy/<page>/.
   - Accessibility: contrast, headings in order, focus states, alt text.
   - Speed: PageSpeed Insights (see agent/research-agent.md).
4. Write qa/YYYY-MM-DD-webflow.md: one line per issue with page, screen size, what is wrong,
   what it should be, and a screenshot name. Ranked: broken first, then off-brand, then polish.
5. Hand the list to the team. Claude does not fix anything in Webflow.

Offer to save to GitHub at the end.
