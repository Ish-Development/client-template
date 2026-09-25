---
name: visual-identity
description: Step 9. Read the client's visual identity from any source the team gives (Figma, HTML files, websites, PDFs, images, code, Webflow) and store it in the kit. Use when the user shares a design source or says "visual identity".
---

# Visual identity

Designers make the visual identity. Claude only reads it and stores it.
Never invent or change a color, font, size, timing, or rule.

## 1. Collect sources
Ask: "Where does the visual identity live? Send links or drop files in
human/visual-sources/. Anything works: Figma, HTML files, websites, PDFs, images, code."
List every source in the Sources table in agent/visual-identity.md: what it is, where it
is, and what it covers (e.g. colors, logo, motion).

## 2. Read each source with the right tool
| Source | How to read it |
|---|---|
| Figma design file | Figma connector: get_variable_defs for variables and styles, get_screenshot for key frames |
| HTML, CSS, JS files | Read the files. Take CSS variables, fonts, colors, and motion: transitions, animations, keyframes, durations, easings, scroll effects. Open in npx agent-browser to see them |
| Website (live) | Public pages only, browsing rules in agent/research-agent.md. Read its CSS the same way |
| Code repo (e.g. Astro) | Read the token, theme, and CSS files |
| Webflow site | Webflow connector: variables and styles |
| PDF guidelines | Read the pages |
| Images | Look at them. Describe only what is visible |
| Lottie (JSON) | Read timings and easings from the file |
| Video | Claude cannot watch video. Ask for the HTML or Lottie source, or a written description |
| Anything else | Ask how to open it. Do not guess |

Motion is usually not in Figma. Expect it in HTML, code, Lottie, or a live site.

## 3. Store
- agent/visual-system.json: the values, keeping the names used in the source.
  Add keys only for what a source has. Empty stays empty.
- agent/constraints-visual.yaml: the rules the designers wrote down.
- agent/visual-identity.md: the identity in words: logo, color use, type use, imagery,
  layout, motion. Each part names its source.

## 4. When sources disagree
Show both values and their sources. Ask which is right. Record the answer in
agent/visual-identity.md. Never pick one silently.

## 5. Report
What was stored, from which source, and what is missing or unclear, as questions for
the designers. Offer to save to GitHub.

When a source changes, run this again. Show what changed before overwriting.
