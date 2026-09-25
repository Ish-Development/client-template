---
name: workshop
description: Read the growth workshop board into the kit after the workshop. Use when the user says "workshop done", shares a FigJam workshop link, or asks to import the workshop.
---

# Workshop import

Reads the client's growth workshop board (FigJam) into /agent as hypotheses.

## Steps
1. Get the board link. Save it in agent/research-brief.md under Workshop.
2. Read the board with the Figma connector (get_figjam). Read every section.
3. Match each block by what it is about, not by its exact name. The board is still
   changing, so names and order can differ. Use this map:

| The block is about | Goes into |
|---|---|
| What the company does, how, what it helps with, results | brand-positioning.yaml (who_we_are, difference, proof_points) |
| Best customers, what they share, the ICP sentence | icp.yaml |
| Who is in the buying room: champion, blocker, influencer, decision maker | buying-committee.yaml |
| Events that start a purchase | triggers.yaml |
| Category or shelf | brand-positioning.yaml (category) |
| Enemy, old way, status quo | brand-positioning.yaml (enemy) |
| POV, the sharp belief | brand-positioning.yaml (pov) |
| Buyer journey, bow tie stages | journey.yaml |
| Which page does which job | site-plan.yaml |

   A block that fits nowhere: list it for the user and ask where it belongs.

4. Ignore template content. Skip:
   - example stickies, e.g. starting with "Ex:" or clearly a sample from another company
   - instruction text, timers, headings, and empty stickies
   - AI summary widgets. Read the stickies, not the summary.
5. Write everything as status: hypothesis, source: workshop YYYY-MM-DD.
   Translate to English. Keep exact quotes in the original language with a translation.
   Keep who wrote a sticky out of the files.
6. Industry-specific notes go in industry_notes per role, not in new roles.

## After
Show a short report:
- What was filled, per file.
- What was empty. Blocker is always listed if empty.
- Where the board disagrees with itself (e.g. two definitions of champion). Ask which is right.
- Where it disagrees with the light research. Add to research/08-risks-and-questions.md.
Then offer: "Want me to run the research pass after the workshop?"
