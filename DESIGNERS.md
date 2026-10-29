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
7. **Follow the interface rules.** `agent/interface-rules.md` part 1: concentric corners, icon lines that match the text, 24px hit areas, image outlines, contrast, spacing between groups. Part 2 is for whoever builds the site.

When a page is ready, send Claude the Figma link to the frame.

---

## New sections: draft first, component last

When a page needs a section that has no component yet, or a new layout for an existing one:

1. **References.** Claude searches Mobbin and sends a few alternatives that fit the page's job. You pick one.
   Jev (the TypeSafe model) does not choose layouts for you: it reads text, not pictures, so for a one-off pick it
   only echoes how Claude described the options. Use it for checks and for choices made many times (every section
   of every page), and only once each layout has a description a person approved. Taste stays with you and the
   designer (user, 2026-10-07, after the How it works test: qa/2026-10-07-jev-trial.md).
2. **Draft.** Claude builds it as a plain frame named `Draft — <section>` in the **Iteration** section on the **Iterations** page ("New components" for new sections, "Replacing existing" for a new version of an existing one, with the current component next to it), desktop and mobile. Only the file's text styles, variables and existing components; no hand-set sizes, weights, colours or gaps. Once a draft becomes a component, move it to Iteration › "Approved — now components" (user, 2026-10-22). After adding or moving any draft, re-lay out every Iteration section (desktop/mobile pairs per row) and restack the sections so nothing overlaps (user, 2026-10-22, third time asked). Mobile uses the same text styles as desktop; the Mobile modes do the sizing.
3. **Iterate.** You comment, Claude adjusts the draft (layout only).
   Copy is written on the page frames in the current sprint page, never in Iteration drafts or main components
   (user, 2026-10-06).
4. **Component.** Only after you say it's right does it become a component variant (desktop and mobile) in its category section, and the draft leaves the Iteration section. A replacement takes the old variant's place.
5. **Tidy.** Put the new desktop and mobile variants next to each other in the set, restack the sets in the section so nothing overlaps, and resize the section.

Decided by the user, 2026-10-05: "dont make component immidietly lets iterate and then go for the component".

---

## Section component rules (Figma)

The rules the team set while building the section components. They apply to people and to Claude.
Claude adds a rule here every time it builds or fixes something (user, 2026-10-06: "always when u build something u
need to think about it, save it to the harness").
Each one says who set it and when; keep a change log in `qa/YYYY-MM-DD-figma-sections-log.md`.
Claude checks these rules with `.claude/scripts/figma-rules-check.js` (read-only) after every draft it builds and
before a draft becomes a component. A new rule here gets a check there when it can be read from the file.

**Styles and sizing**
- Only the file's text styles and variables: type, colour, spacing, radius. No hand-set sizes, weights, hex colours
  or pixel gaps. Headings use the bold styles. (Mohammed, 2026-10-05)
- Mobile uses the same text styles as desktop. Every mobile variant gets the Mobile modes for Sizes and Typography,
  every desktop variant the Desktop modes; the modes do the sizing. Never pick a smaller or lighter style for mobile.
  (2026-10-02, 2026-10-05)
- Spacing is the same on every breakpoint: desktop and mobile use the same spacing variables (section-space, space,
  grid/gutter, grid/margin) for the same element; the Mobile mode makes them smaller. (user, 2026-10-06)
- Every draft frame gets the layout grid the components use (columns bound to grid/Columns, grid/gutter, grid/margin; desktop and mobile), so widths can be checked against it (user, 2026-10-22: "always add the grid when iterating").
- Icons in lists and rows lie flat beside the title: the plain line icon, no box, coloured with a variable; stacked: icon on top, then title, then text, all left aligned (gap space/4, then space/2). Ruled rows on desktop may keep icon + title beside the text. Icons in a grid of cells sit in the Icon badge (Type=Icon) with the icon swapped in (user, 2026-10-22).
- Image beside a text card: the image sets the height, the text card fills it; inside the card the headline sits at the top and the text (and button) at the bottom, space between. No fixed gap and no fixed section height (user, 2026-10-22, after inspecting a reference site). When stacked on mobile, or when the card floats on a photo, nothing pushes it: stack top-down with gap space/12 (Section heading Layout=Card). Images beside text (Hero Split, CTA Side image, Layouts / Split) are 4:3 on desktop and mobile. CTA sections have one button.
- Every heading and paragraph sits in a `Heading wrapper` / `Paragraph wrapper` (vertical, fill) bound to its width variable: section level `heading/max-width` / `text/max-width`, items and cards `card-heading/max-width` / `card-text/max-width`. Claude adds them on every build, drafts included (user, 2026-10-22: "always always add paragraph width also pleae").
- Lines between cells and around grids use `Border/border-primary`, not an alpha colour. No hand-set padding to create an effect (e.g. a stagger): if the effect needs a value, it must come from a space variable (user, 2026-10-22: "u were messing up the spacing and the border variables").
- Give layers unique, meaningful names inside a component (Title, Body, Label, not two layers called "Paragraph").
  Checks and fixes match desktop to mobile by layer name; duplicate names caused wrong matches on 2026-10-06.
- Column widths (Heading width / Text width, 3–12 col) go on wrapper frames, never on text. Text fills its wrapper.
  Heading and paragraph wrappers that sit side by side with something else get their width from the variable;
  otherwise they fill with a max width. (2026-10-02, 2026-10-05)
- Card and layout sections: card paragraphs sit in a "Paragraph wrapper" (max width card-text/max-width) and card
  titles in a "Heading wrapper" (max width card-heading/max-width). Two settings on the section, 3–12 col, default
  12 col (no limit): Card heading width and Card text width. Select the section instance and set them in the right
  panel, next to Heading width and Text width (those stay for the section heading). Never resize a card text by hand.
  (user, 2026-10-06: "need to be able to work with the widths of the paragraph …", "dont see it", "cant change card
  heading width")
- The four width settings are named with a letter so they sit together, in reading order, at the top of the right
  panel's modes (above Sizes and Typography): "A. Heading width", "B. Text width", "C. Card heading width",
  "D. Card text width". A new width setting gets the next letter. Renaming a collection keeps every binding and
  every chosen mode. (user, 2026-10-15, from another project)
- On the Sections page, each group (Hero, Features, Contact …) is an auto-layout frame that hugs its component
  sets, not a Figma section, so new variants never spill outside it (user, 2026-10-15).
- Rows of side-by-side parts (tabs, image, text) sit on the 12-column grid with grid/gutter gaps, not space-between
  with a hugging text column; a hugging column can't take a max width. (2026-10-06)
- Heroes have their own layout. Don't force grid or column rules onto them. (2026-10-06)
- Every section variant has the "Grid" layout grid style: 12 columns on desktop, 4 on mobile. (2026-10-06)

**Structure**
- Never clip content on heading or paragraph wrappers, or any frame that only holds text. (2026-10-06)
- Empty wrappers are hidden as a whole, so they take no space. Turning a button off collapses its row. (2026-10-02,
  2026-10-06)
- Shared parts (Section heading) carry no width modes of their own; the section decides. (2026-10-02)
- Use component properties and modes, not manual overrides on instances.
- After an icon swap, check the icon's colour variable is still linked. (2026-10-05)

**Images**
- Every image area in a section component is a slot ("Image 1", "Image 2", "Avatar 1"), so a photo or illustration
  can be dropped in on the instance. The slot is a plain frame, never auto layout (user, 2026-10-06: "dont make the
  image slots auto layout"); it clips, and its image is set to the slot's size with Scale (stretch) constraints and an
  image fill set to Fill, so it crops, never distorts. When a draft becomes a component, its image areas become slots.
  (2026-10-06)
- An image keeps its aspect ratio on every breakpoint: the mobile image area has the desktop ratio at the mobile
  width (e.g. 3:2 stays 3:2, square stays square). Exceptions: full-bleed hero backgrounds, and cards that fill
  leftover height on desktop (Big cards). Where desktop mixes card sizes in a mosaic, mobile cards all use the main
  card ratio, full card width. (user, 2026-10-06)
- Illustrations stay the real ones. Until the photographer delivers, photos are a plain colour block. (2026-10-05)

**Copy that survives a layout switch** (user, 2026-10-07)
- Group components by the kind of copy they hold, not by how they look. Layouts that hold the same kinds of copy are
  variants of one set (Type = layout, Breakpoint = desktop/mobile); a layout that needs different copy (steps with
  points and stats vs cards) is a separate set, because switching to it means writing new copy.
- Copy lives in shared text properties with the same names in every set: Heading, Intro, Item 1–6 title / subtitle /
  text; the slider has Stat, Stat label, Quote, Name, Title. Switching the Type keeps the copy. The section heading
  sits in a nested "Section heading" instance and keeps its text as long as every layout names it "Section heading".
- Optional elements are on/off switches, never hidden layers: Item N link, Card labels, Step subtitles, Step stats,
  Step points, Step 4, Show quote, Channels marquee, Country tabs. The switch sits on the element's wrapper, not on the
  text inside it, so the space closes. (user: "u are disabling visiablity on the eyebrow and not on its wrapper")
- Inside a stack that hugs its height, children hug too (never Fill), so a card shrinks when a link or label is off.
  (user: "why isnt the card collapsing when the link is turned off?")
- Every link switch must close its space, in all sections and all cards (user, 2026-10-07: "make sure the things
  collapse when i turn off the links this goes for ALL section and ALL cards"). In a row of cards, the first card hugs
  and the others fill. Where a photo sets the row height (Steps, Progress on desktop), the text block above the link
  still closes up. Test: switch all links off on an instance; every frame holding a link must shrink.
- One placeholder text per property (the original sample copy), so layouts in a set share their sample text.

**Grids of cards**
- Card counts fit the columns: a 2-column grid holds 4 or 6 cards, a 3-column grid 3 or 6. (2026-10-06)
- Cards side by side get near-equal word counts.
- Cards side by side line up: in a row, every image area has the same height, so labels and titles start at the same
  line; links sit at the bottom of the card, so they line up too. The card with the most text sets the row height
  (hug), the others fill the row. (user, 2026-10-06: "looks weird that the text boxes are different height so the text
  is not aligned between the boxes")

**Two Figma files** (user, 2026-10-07: "we have a figma file for the client so we can work in peace")
- Internal, where we work: [CLIENT_NAME (Internal)](PUT-INTERNAL-FIGMA-LINK-HERE), copied from the Ish starter file
  "Client Name – Website Design Foundation (Internal)". Sections page (approved components only), Iterations page
  (drafts) and one page per sprint.
- For the client to see: [CLIENT_NAME – Website Design Foundation](PUT-CLIENT-FIGMA-LINK-HERE): the pages, copied over
  from the internal file when they are ready to show.
- The two files don't sync. Claude changes only the internal file; the user copies pages and notes over to the
  client's file when they are ready, so no double work is needed (user, 2026-10-12). Drafts, variations and pages the
  client shouldn't see yet stay internal only.

**Organising the file**
- Category sections on the Sections page, named and ordered like Mobbin's section categories: About, Blog, CTA,
  Contact (including the people grids), FAQ, Features (including How it works and Benefits), Hero, Layouts (general text and image layouts, user 2026-10-22), Social Proof (add 404, Comparison, Newsletter,
  Stats… only when a component exists), then the approved components only. Drafts live on the Iterations page, and small shared parts on their
  styleguide page: Section heading on Typography, Carousel controls on Buttons, FAQ item on Dropdown (user, 2026-10-12:
  "create a page for iterations so the sections page dont get messy only approved stuff lands there"). One component set per kind of copy (see "Copy that
  survives a layout switch"), desktop and mobile variants side by side, each layout's pair on its own row. Navbar and
  Footer stay on their own Navigation page. (2026-10-06, 2026-10-07)
- Component pages (styleguide) use the Buttons page layout: bg-secondary background, title and note on the left in
  text-primary, components on the right. (2026-10-05)

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

## Fluid sizes

Figma can't do clamp. Put fluid type and spacing in Webflow variables or in code, with clear names:
```css
:root {
  --text-body: clamp(1rem, 0.9rem + 0.5vw, 1.25rem);
  --space-section: clamp(4rem, 3rem + 4vw, 8rem);
}
```
Claude copies them exactly as written into `agent/visual/tokens.json`. In Figma, use the size at your design width.

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
