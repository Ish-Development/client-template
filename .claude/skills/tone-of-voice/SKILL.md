---
name: tone-of-voice
description: Step 7. Build the client's VOICE.md and STYLE.md with Compound Writing, from the client's own writing or, if they have no voice yet, from inspiration websites. Use when the user says "tone of voice", "voice", or "let's do the voice".
---

# Tone of voice

Load the tone_of_voice files from agent/retrieval-rules.yaml first.
This step wraps Compound Writing. If cw-onboarding is not available, tell the user:
"Compound Writing is not installed. Accept the plugin prompt when opening this folder,
or run /plugin install compound-writing@compound-writing, then start a new session."

## 1. Gather examples
Put everything in copy/examples/, one file per source, with the URL and date.
- The client's own writing: current website copy, founder posts and interviews,
  workshop quotes (from agent/ and research/). Mark as: client.
- Competitor copy from research/04-competitors.md. Mark as: negative, how we do not
  want to sound.

## 2. Ask which path
"Does the client have a voice worth keeping?"
- Yes: go to 4 and calibrate from the client's examples.
- No, or not sure: go to 3.

## 3. No voice yet: inspiration sites
1. Ask: "Which websites should I look at for inspiration? Paste 2-5 links, and say what
   you like about each if you know."
2. Read each site like a buyer would: home page and 2-3 key pages. Public pages only,
   follow the browsing rules in agent/research-agent.md.
3. Write copy/examples/inspiration.md. For each site: URL, date, and the voice moves you
   observed: sentence length, rhythm, word choice, how headlines and buttons are written,
   how they handle proof. Short quotes only, to show a move.
4. Inspiration is direction, never material. Never reuse their phrases, claims, or
   structure word for word. Mark every quote in the file as: do not reuse.
5. Write 3 voice directions. Each one:
   - a name and 2-3 lines describing it as tensions ("direct without being blunt")
   - which inspiration site and which buyer role it leans on
   - the same sample lines in that voice: homepage headline, button, error message,
     email subject, one short paragraph about what the client does
   Check samples against constraints-messaging.yaml and brand-positioning.yaml.
6. The user picks one, or mixes ("A, but drier"). Write the choice down in
   copy/examples/inspiration.md.

## 4. Build VOICE.md and STYLE.md with cw-onboarding
Run cw-onboarding with these instructions:
- Writing home: agent/VOICE.md and agent/STYLE.md. Examples: copy/examples/.
  Drafts: copy/<page>/. Do not create other folders or files.
- Audience: use agent/buying-committee.yaml and agent/icp.yaml. Do not create AUDIENCE.md.
- Calibrate from the client examples (path 2) or the chosen direction and its
  inspiration notes (path 3). Competitor examples are what to avoid.
- STYLE.md must keep: page structure by job (agent/site-jobs.md), claims and proof,
  calls to action, and the ready-to-publish checklist.
Show the drafts. The user edits.

## 5. Test on a real section
Pick one section from sitemap/index.html, usually the home page hero. Write it in the
voice into copy/<page>/draft-version-one.md. Run cw-voice-check and cw-ai-check.
Show the result and what the checks found.

## 6. Keep learning
When the user corrects the voice in later work, offer cw-save so the lesson becomes a rule
in VOICE.md or STYLE.md.

## Internal
Tone of voice stays internal. There is no client sign-off here. The client reacts to the
voice when design and copy are presented together. That feedback comes back through the
client-feedback skill.

Offer to save to GitHub at the end.
