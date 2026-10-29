# Interface rules

Rules for every interface we make, on every project: in Figma, in the build (Webflow, Astro) and in the words on
buttons, labels and empty states. They hold for every client. The client's own look lives in agent/visual/.

Source: a public interface cheat sheet, adopted by the team on 2026-10-29. Rewritten in our words; the Figma notes
say how each rule shows up in the Figma starter file.

Who uses this:
- Designers and Claude in Figma: part 1.
- Whoever builds the site: part 2 (part 1 too, so the build matches the design).
- Whoever writes copy or reviews it: part 3.
- Design critique (design-qa) checks all three.

---

## 1. Design (Figma)

**Shape and alignment**
- Nested corners are concentric: outer radius = inner radius + the padding between them. If the padding is as big as
  the outer radius, the inner element is square (`radius/none`). Big padding (much more than the radius) can keep its
  own radius.
- Align by eye, not only by the numbers. A play triangle, an arrow or a round icon can need a nudge to look centred.
- A button with an icon has slightly less padding on the icon side. In Figma: the text sits in a "Text padding"
  wrapper, so the text side gets the button padding plus the wrapper padding.
- Give depth with soft layered shadows, not with borders. Elements that float over photos or mixed backgrounds get
  the "Hairline ring" effect (1px, black 5%) instead of a grey stroke. Plain backgrounds can keep a normal border.
- Every image gets a 1px outline on the inside: black 8% in light mode, white 8% in dark (`Border/border-image`), so
  it doesn't bleed into the background.
- Match an icon's line to the text beside it: 2px next to Medium text (buttons, links, nav, accordion), 1.5px next to
  Regular text and on its own (`icon/stroke-medium`, `icon/stroke-regular`). Use the icon size that exists
  (24, 20, 16, 12); never scale an icon to an in-between size, because that changes its line width.

**Spacing**
- Leave at least twice as much space between groups as between items in a group (for example 8px inside, 16px or more
  between).
- Things people click are at least 24×24. Aim for 40×40 on desktop and 44×44 on touch. Small marks (slider dots,
  close icons) get invisible padding to reach that. Hit areas never overlap.

**Text**
- Long text (articles, legal, long answers) runs 60–75 characters per line. In Figma: set Text width to about 5–6
  columns for article body.
- Type text in normal capitalization. Show uppercase with the text style's case setting (as Eyebrow does), never by
  typing capitals.
- Use real punctuation: curly quotes, an en dash for ranges (2–4 weeks), an em dash for an aside, and the ellipsis
  character (…) instead of three dots.
- If text is cut short with an ellipsis, there is a way to read all of it (tooltip or expanded view).

**Colour**
- Components use role variables (Text, Background, Border, Foreground, component roles), never primitives.
- Every step in a palette has a job (page background, hover, border, solid fill, body text). Delete steps nothing uses.
- Name colours by what they do (`bg-brand-solid`), not by where or what they look like (`blue-button`, `sidebar-grey`).
- Dark mode gets its own values; it is not the light mode turned upside down. One way to switch themes: variable
  modes (Light, Dark, Brand).
- Check contrast against what is directly behind the element: 4.5:1 for text, 3:1 for large text, icons and the edges
  of form fields.
- Never show a status with colour alone. An error also has an icon and a message; a checked box has a check.

**Forms and controls**
- Every input has a visible label (keep the Label switch on). Placeholder text is a hint, not the label.
- Focus is always visible ("Focus ring" style). Never remove it without a replacement.

---

## 2. Build (Webflow, Astro, code)

**Focus and interaction**
- Use the real element: `<button>` for actions, `<a>` for links. They come with keyboard and screen reader behaviour
  built in.
- Style `:focus-visible`, not `:focus`. Never remove the outline without putting the focus ring in its place.
- Only `tabindex="0"` or `tabindex="-1"`. Positive numbers break the tab order.
- Put hover styles inside `@media (hover: hover)`. On touch screens a hover stays stuck after a tap and looks selected.
- Decorative layers (glows, gradients, overlays) get `pointer-events: none`, so they never block a click.
- Hit areas at least 24×24 (40 desktop, 44 touch), never overlapping.

**Forms**
- Every input has a `<label>`. Set `type` and `inputmode` to what people should type (email, tel, numeric).
- Never block paste. People paste passwords and one-time codes.
- Keep the submit button enabled until the request starts. Check for errors on submit, mark invalid fields with
  `aria-invalid="true"`, link each error message with `aria-describedby`, and move focus to the first invalid field.

**Screen readers**
- Icon-only buttons get a clear `aria-label` ("Next slide", not "Arrow"). Never put `aria-hidden="true"` on something
  that can be focused.
- Alt text says what the image shows and why it's there. Decorative images get `alt=""`.
- Routine updates use `role="status"`. Save `role="alert"` for urgent errors.

**Motion**
- Respect reduced motion: put animations inside `@media (prefers-reduced-motion: no-preference)`.
- Name the properties you animate (`transition: opacity 200ms, transform 200ms`). Never `transition: all`.
- Use transitions for interactions, so they can reverse halfway. Use keyframes for one-off sequences.
- Things animate from where they were triggered (set `transform-origin` toward the trigger), not from the centre.
- Exits are quieter than entrances: shorter distance, fade out with a small blur (about 4px).
- Menus people open often open instantly; animate only the close.
- Frequent interactions (hover colour, toggles) are instant or very fast.
- Buttons press in slightly: `scale(0.97)` (0.95–0.98) with about 200ms ease-out.
- When an icon swaps (menu to close), cross-fade: the new one scales from 0.25 to 1, fades in and un-blurs from 4px;
  the old one does the reverse.
- When many things enter, animate them in small groups with a short delay, not as one block.
- No animation on page load unless it's on purpose.
- Turn transitions off while switching between light and dark mode.
- If something shifts 1–2px while animating (often in Safari on iOS), add `will-change: transform` to it.

**Type**
- Fonts as `.woff2` only, never `.ttf` or `.otf`.
- Numbers that change or line up (prices, stats, counters, tables) use `font-variant-numeric: tabular-nums`.
- Headings get `text-wrap: balance`, short descriptions `text-wrap: pretty`. Long text gets neither.
- Long words, links and IDs stay inside their box: `overflow-wrap: break-word`. Labels and badges that must stay on
  one line: `white-space: nowrap`.
- Set `-webkit-font-smoothing: antialiased` and `-moz-osx-font-smoothing: grayscale` on the root.
- Underlines skip the tails of letters: `text-underline-position: from-font` and `text-decoration-skip-ink: auto`.
- Uppercase comes from `text-transform`, not from typed capitals.

**Layout and colour**
- Headings people can link to get `scroll-margin-top`, so the sticky nav doesn't cover them.
- Colours are CSS variables named by role. One way to switch themes: either `prefers-color-scheme` or a class
  (`.dark`, `.brand`), never both.
- Gradients: say how colours mix. `in oklab` for even brightness, `in oklch` for brighter middles, `in srgb` for more
  muted ones.

---

## 3. Words in the interface

- Buttons start with a verb and say what happens: "Book a call", "Download the guide". Never "OK", "Yes" or "Submit".
- A confirm button names the action ("Delete project" next to "Cancel").
- One word for "next step" across a whole flow: pick "Continue" or "Next" and keep it.
- Links say where they go ("See our pricing", not "Click here").
- Capitalize buttons, headings and labels the same way everywhere. Sentence case is the default ("Book a call").
- Toggles are labelled with what happens when they're on ("Send me updates", not "Disable updates").
- An empty view says what belongs there and gives one action to start.
- Talk to the reader as "you", never "the user".
- The client's own words and tone (VOICE.md) win where they differ, except for clarity and accessibility.
