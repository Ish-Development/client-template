---
name: positioning
description: Step 5. Turn workshop output and research into the brand's positioning, one decision at a time, then write a summary for client sign-off. Use when the user says "positioning", "let's do positioning", or after deep research is done.
---

# Positioning

Load the positioning files from agent/retrieval-rules.yaml first.
If research/00-overview.md does not say the deep pass is done, say so and ask whether to continue anyway.

## 1. Agreements first
Compare the workshop output (status: hypothesis) with the deep research
(research/05-audience.md, 06-brand-implications.md).
Where they agree and research has a source: update the file, set status: validated,
and add the source IDs. Show a short list of what you validated.

## 2. Decisions, one at a time
Where the workshop and research disagree, or research found nothing:
- Ask one question at a time. Plain words. Show what the workshop said, what the
  evidence says, and the source.
- Offer 2-3 clear choices, plus "leave open".
- Write the answer into the file. "Leave open" stays hypothesis and goes to
  research/08-risks-and-questions.md.
Order: ICP, buying committee (blocker always included), triggers, category, enemy.

## 3. Core lines: 3 options each
For one_liner, difference, and pov in brand-positioning.yaml:
- Write 3 options, each different in angle, not just wording.
- Under each: one line on what it emphasises and which buyer role it speaks to.
- Check each against constraints-messaging.yaml and the words to avoid in VOICE.md.
- The user picks, edits, or asks for more. Write the chosen line into the file.
Also draft brand-values.yaml: internal and customer-facing, 3-4 each, for the user to edit.

## 4. Client sign-off
Write human/positioning-summary.md for the client. One page, plain words, no internal notes:
- Who you are for (the ICP sentence)
- Who buys, and what each of them needs
- The shelf you sit on, the old way you fight, what you believe
- The one-liner
- What is still open, as questions for the client
Then say: "Positioning is drafted. Send human/positioning-summary.md to the client for
sign-off before the site plan." Record sign-off in brand-positioning.yaml as
signed_off: YYYY-MM-DD when the user confirms it.

## Rules
- Never invent proof. proof_points only from research/sources.md or client confirmation.
- Do not skip a decision because it seems obvious. The user decides.
- Offer to save to GitHub at the end.
