---
name: client-feedback
description: Sort client feedback to the step it belongs to and update the kit. Use when the user pastes client feedback, says "the client said", or after presenting design and copy together.
---

# Client feedback

The process moves like a spine: feedback on one step can move the others.
Tone of voice is internal until the client sees design and copy together, so most
voice feedback arrives here.

## Steps
1. Read the feedback. Split it into single points. Keep the client's exact words.
2. Sort each point to where it belongs:

| The point is about | Step | File |
|---|---|---|
| How it sounds: words, tone, rhythm | Tone of voice | agent/VOICE.md (via cw-save) |
| What the copy says, claims, proof, page structure | Tone of voice / Copy | agent/STYLE.md, copy/<page>/ |
| Who it is for, what we stand for, the one-liner | Positioning | agent/brand-positioning.yaml |
| Which pages exist, what each page does | Site plan | agent/site-plan.yaml, sitemap/ |
| Colors, type, layout, imagery | Visual identity / Design | agent/visual/, the design sources |
| A fact about the business we got wrong | Research | research/, then the file that used it |

3. Show the sorted list. For each point: what you would change, and which later steps
   it touches (e.g. a positioning change means copy must be checked again).
4. Ask before changing anything. Change one step at a time, starting with the earliest.
5. Voice lessons: offer cw-save so they become rules in VOICE.md.
6. Log the round in copy/feedback.md: date, who gave it, the points, and what changed.
   Refer to people by role, not name.

Offer to save to GitHub at the end.
