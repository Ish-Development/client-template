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
3. Check against the kit:
   - Visual system: colors, type, spacing, radius, effects match agent/visual/tokens.json.
     Flag values that are off-token or not bound to a variable.
   - Rules: Hard rules in agent/visual/usage.md. Components match agent/visual/components.html.
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
   - Motion matches agent/visual/motion.json and agent/visual/usage.md.
   - Links: no broken links or 404s.
   - SEO: page title, meta description, one H1, alt text, per copy/<page>/.
   - Accessibility: contrast, headings in order, focus states, alt text.
   - Speed: PageSpeed Insights (see agent/research-agent.md).
4. Write qa/YYYY-MM-DD-webflow.md: one line per issue with page, screen size, what is wrong,
   what it should be, and a screenshot name. Ranked: broken first, then off-brand, then polish.
5. Hand the list to the team. Claude does not fix anything in Webflow.

Offer to save to GitHub at the end.
