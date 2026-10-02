---
name: kit-test
description: Test the kit with a fresh agent. A subagent with no project context makes something nobody has designed yet, from /agent only, and lists every decision. Each guess shows a gap in the kit. Use when the user says "test the kit" or "kit test", and offer it after tone of voice and after visual identity.
---

# Kit test

Give the kit to a fresh agent with no other context. Ask it to make something nobody has
designed or written yet. Every guess it makes points at a gap in the kit.
Fix the kit, not the output.

The test output is a probe, not work. Never show it to the client. Never use it as
design or copy. Claude still builds nothing for the client.

Load the kit_test files from agent/retrieval-rules.yaml first.

## 1. Check the kit is ready
Two kinds of test:
- Copy test, after tone of voice: needs brand-positioning.yaml, VOICE.md, STYLE.md,
  and constraints-messaging.yaml filled.
- Full test, after visual identity: also needs visual/tokens.json and the visual topic
  files filled (see visual/usage.md).
If a file the test needs is still blank, say which one and stop. A test on a blank kit
only finds the blanks.

## 2. Pick the tasks
Suggest 2-3 tasks the kit has not been used for yet. The user picks or changes them.
- One page or section from agent/site-plan.yaml with no design or copy yet.
- One piece outside the site: a launch email, an ad, a social post.
- Full test only: the same page as an HTML screen.
Each task uses one key from agent/retrieval-rules.yaml, e.g. homepage, product_page,
ads_or_social, support_copy, ui_or_landing_build. Write the key down.

## 3. Run the fresh agent
One subagent per task (Agent tool, general-purpose), all at once. It gets nothing from
this conversation. Give it only this prompt, filled in:

```
You are new to this brand. Make: <task>.
1. Read agent/retrieval-rules.yaml. Load only the files listed under <key>.
2. Read nothing outside agent/. Not research/, copy/, human/, sitemap/, qa/, examples/.
3. Make it. Copy as text. A screen as one HTML file using the values in agent/visual/tokens.json.
   Save it to qa/<date>-kit-test-<task>.<md or html>.
4. Below it, list every brand decision you made: words, claims, tone, color, type,
   spacing, layout, imagery, motion. One per line:
   decision | file and section it came from, or GUESSED | what you would have needed to know
Do not hide guesses. A guess is useful.
```

## 4. Check every decision
Read the output and its decision list against the kit. Give each decision one label:
- Right: the file it names says so.
- Missed: the kit has the rule, but the agent did not load it, did not find it, or broke it.
- Guessed: the kit has no rule for it.
Check the output against constraints-messaging.yaml and the Hard rules in the
agent/visual/ topic files, even where the agent says Right.
Ignore guesses that are the task itself, like the exact words of a headline. Count the
ones the brand should have decided: what a color is for, a banned word, a claim, the tone,
a layout or image rule.

## 5. Fix the kit
Show each proposed fix. Apply it only after a yes, one at a time.
- Missed, file not loaded: add the file to that key in agent/retrieval-rules.yaml.
- Missed, file loaded: make the rule clearer. Same meaning, never a new rule.
- Guessed: the kit does not hold this decision yet. Never fill it in.
  - Visual: add it to Open questions for the designers in agent/visual/usage.md.
  - Voice or copy: ask the user. Write the answer in VOICE.md or STYLE.md, with its why.
  - Facts and claims: add to research/08-risks-and-questions.md.

## 6. Report
Write qa/YYYY-MM-DD-kit-test.md:
- Each task, its retrieval key, and the output file.
- Count per task: right, missed, guessed.
- Each missed and guessed decision: what it was, the fix, and its status (applied, or
  open question and who answers it).

Then ask: "Run it again with a fresh agent and the same tasks?" Repeat until the only
guesses left are open questions someone else has to answer.

Offer to save to GitHub at the end.
