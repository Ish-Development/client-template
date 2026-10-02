# Visual

The visual identity in a form Claude can use. Delivered by designers, collected and
organised by Claude (visual-identity skill). Claude builds nothing here.

| File | What it is | Who makes it |
|---|---|---|
| tokens.json | Colors, type, radius, space. The knobs. | Claude copies from the sources |
| tokens.css | The same values as CSS variables, for coded sites (Astro). | `npm run tokens`. Never edit by hand |
| usage.md | Start here: which file to read for which job, sources, decisions, open questions | Claude writes from the sources |
| logo.md, color.md, typography.md, imagery.md, layout.md, components.md, motion.md | How each part is used, with the hard rules and why | Claude writes from the sources |
| components.html + components.css | Real buttons, heroes, cards, type, spacing. The spec, not a screenshot. | Designers. Empty if not delivered |
| logo.svg, icons/ | Geometry Claude can redraw. SVG, never PNG. | Designers, or exported from Figma |
| motion.json | Easing curves, durations, hover and page transitions. One flat file. | Claude copies from HTML, code, Lottie, or a live site |
| demos/ | Working HTML pages: a landing or motion demo to click through | Designers |

Not here: final client PDFs, Figma screenshots, moodboards as images only, long strategy
essays. Those stay in /human.
