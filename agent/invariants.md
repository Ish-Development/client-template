# Rules that hold everywhere

The few rules that must be true on every surface: copy drafts, the sitemap, Figma, Webflow and the
client's Google Docs. Each has an ID, where it comes from, and what checks it. "Nothing yet" means only
people and prose guard it: a check to build. Edit in place when a rule changes; the commit says why.

A rule here never gets an "except when". If a case needs a different rule, name it as its own rule.

## Pages
- **P-1 Every page has one job and one next action.** Source: agent/site-plan.yaml, CLAUDE.md.
  Checked by: jev-design-check.py "Next action" (Figma, run by hand in design-qa). Sitemap and Webflow:
  nothing yet.

## Copy
- **C-1 No invented claims or numbers. Every fact has a source, or a "To confirm" line.** Source: CLAUDE.md
  rule 4, constraints-messaging.yaml. Checked by: jev-copy-review.py "facts to check" (drafts, on every
  save). Figma and Webflow: nothing yet.
- **C-2 The copy in Figma and the draft it came from agree.** Source: copy and design-qa skills.
  Checked by: jev-design-check.py "Draft match" (run by hand in design-qa).
- **C-3 The sites we take inspiration from are never named.** No names, URLs or brand words.
  Source: CLAUDE.md. Checked by: nothing yet.
- **C-4 The voice rules hold: no banned words, no colons in headings.** Source: VOICE.md.
  Checked by: jev-copy-review.py (drafts, on every save), figma-rules-check.js copy rules (Figma, by hand).
  Webflow: nothing yet.

## Images
- **I-1 No AI-generated photos in anything the client gets.** Real photo and video come from the client
  or our production partners. Source: Ish organisation rule. Checked by: nothing yet.

## Design
- **D-1 Figma uses only the file's text styles and variables.** No hand-set sizes, colours or gaps.
  Source: DESIGNERS.md. Checked by: figma-rules-check.js (by hand, after every draft).

## Reach
- **R-1 Webflow is read-only for Claude.** Source: CLAUDE.md, design-qa skill. Checked by:
  .claude/settings.json blocks the Webflow build tools and asks before every other Webflow call.
- **R-2 Claude never shares a Google Drive file.** Source: CLAUDE.md. Checked by: .claude/settings.json
  blocks sharing.
- **R-3 One client's material never goes into another client's work.** Source: Ish organisation rule.
  Checked by: nothing yet.
- **R-4 Claude changes only the project's own Figma file** (the internal link in DESIGNERS.md). Source: CLAUDE.md.
  Checked by: .claude/hooks/figma-file-guard.py asks before any change in another file, or while the link is blank.

## Saving
- **S-1 Every commit says the decision and why.** Source: CLAUDE.md. Checked by: jev-commit-guard.py
  (blocks the commit).
