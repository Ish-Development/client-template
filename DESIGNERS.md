# For designers

How designers work with the kit: what to read before you start, how to set up hi-fi and motion so Claude can read them, and where to save your files.

Claude does not design or build. It reads your work, keeps the kit in sync, and checks the design against the plan.

---

## Before you design

Open the client folder and read these. Or ask Claude: `give me a design briefing`.

| Read | Why |
|---|---|
| `sitemap/index.html` | Every page, its job, and its wireframe with the copy in it. Open it in the browser |
| The Positioning summary in the client's Drive folder | Who it's for and what the brand stands for |
| `agent/VOICE.md` | How the brand sounds. The design should feel like the words |
| `agent/visual/usage.md` | The visual identity so far, if there is one |

Words come first. Design around the real copy in the wireframe, not placeholder text.

---

## Hi-fi in Figma

Set up the file so Claude can read it and check it.

1. **Use variables for every value.** Colors, type, spacing, radius, effects. Claude reads variables into `agent/visual/tokens.json`, and the design critique flags anything that is not on a variable.
2. **Name pages after the site plan.** One Figma frame per page, named as in `sitemap/index.html` (Home, Product, Contact).
3. **Name sections as in the wireframe.** Hero, Stats, CTA section. The names come from `agent/section-library.md`.
4. **Name components the same way.** A component called `Contact module` in Figma is the `Contact module` in the section library.
5. **Write your rules on the canvas.** Logo clear space, color use, what never to do. Claude reads them into the hard rules.
6. **Logos and icons as vectors.** Claude exports them as SVG. Never only PNG.

When a page is ready, send Claude the Figma link to the frame.

---

## Motion

Motion is usually not in Figma. Build it where it can run:

- **HTML and CSS** (preferred). Put timings and easings in CSS variables with clear names:
  ```css
  :root {
    --ease: cubic-bezier(0.22, 1, 0.36, 1);
    --buttonHover: 180ms;
    --heroFade: 600ms;
    --page: 420ms;
  }
  ```
- **Lottie** (JSON) for illustrations and animated icons.
- **A live prototype** (a link Claude can open).

Claude reads the names and values exactly as you wrote them into `agent/visual/motion.json`. It can't watch video, so send the HTML or Lottie file, not a screen recording.

---

## Components in HTML

If you build components in HTML and CSS (buttons, heroes, cards, type, spacing), deliver them. Claude copies them to `agent/visual/components.html` as the spec. Working landing pages or motion demos go in too; Claude keeps them in `agent/visual/demos/`.

---

## Save your files in the project

You don't need to know Git. Three steps:

1. **Drop your files** in the client folder, in `human/visual-sources/`:

   | Put it in | What |
   |---|---|
   | `human/visual-sources/motion/` | HTML, CSS, JS, or Lottie motion studies |
   | `human/visual-sources/components/` | HTML and CSS components |
   | `human/visual-sources/demos/` | Working HTML pages |
   | `human/visual-sources/svg/` | Logos and icons as SVG |
   | `human/visual-sources/guidelines/` | PDF brand guidelines |

   Figma files and live sites don't need to be saved. Just send Claude the link.

2. **Open the client folder in Claude** and say: `visual identity`. Claude reads everything, organises it into `agent/visual/`, and asks you about anything unclear or contradictory.

3. **Say `save my work`.** Claude shows what changed and saves it to GitHub after you say yes.

Every time you open the project, Claude gets the latest version first, so you always work on your colleagues' newest files.

---

## Design critique

Before a design goes to the client or to build, say `design critique` and send the Figma link.

Claude checks it against the kit: variables, sections in the right order, the page's next action visible, the copy matching the approved copy, consistency, contrast, and text size. It writes the findings in `qa/`.

- **Small fixes** (a missed border radius, spacing off the scale, a color not on a variable): Claude asks before fixing them in Figma. Say yes to the ones you want, or fix them yourself.
- **Design questions** (layout, hierarchy, imagery): critique only. Claude never changes them.

---

## Client feedback

The client sees design and copy together. Paste what they said, or let Claude read their comments in the Drive docs, and say `client feedback`. Claude sorts each point to where it belongs (design, copy, voice, site plan, positioning) and asks before changing anything.

---

## After the build

When the team has built the site in Webflow, say `QA the site`. Claude checks the live site read-only, at mobile, tablet, and desktop, including motion against `motion.json`, and writes a ranked list of issues. The team fixes them.
