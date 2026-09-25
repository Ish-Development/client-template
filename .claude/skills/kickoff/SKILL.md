---
name: kickoff
description: Start a new client project. Use when the user says "let's go", "kickoff", "start", or "new client", or when agent/research-brief.md is still blank. Interviews the user for the research brief, writes it, and sets the client name across the kit.
---

# Kickoff

Interview the user to fill agent/research-brief.md. Then set up the kit for this client.

## Before asking anything
1. If this folder is named client-template, this is the template. Do not fill it in. Instead:
   a. Ask: "What is the new client called?"
   b. Make a short folder name from it: lowercase, dashes, e.g. "Clarify AS" -> clarify.
   c. Say what you will do and wait for a yes:
      "I'll create a private GitHub repo Ish-Development/<name> from the template and
      download it next to this folder. OK?"
   d. On yes, from the parent folder run:
      gh repo create Ish-Development/<name> --template Ish-Development/client-template --private --clone
      then: gh repo edit Ish-Development/<name> --add-topic client-kit
   e. Say: "Done. Open the <name> folder in Claude and say let's go."
   Stop here.
2. If node_modules/agent-browser is missing, run npm run setup.
3. Read agent/research-brief.md. If it already has answers, show what is filled and ask only about the gaps.

## How to ask
- Ask 2 to 4 questions per round. Never all at once.
- Plain, short questions. One line each.
- "Don't know" and "skip" are fine answers. Leave that field blank. Never guess.
- After each round, say in one line what you wrote down.

## Rounds
Round 1: the basics
- What is the client called?
- What is their website?
- What are we doing: brand, website, or both?
- Is there a deadline?
- Who writes the copy: us or the client?

Round 2: the company
- Any other links? LinkedIn, press, app store.
- Who are the founders?
- Which industries do they sell to?
- Do we have access to their Google Search Console or analytics?

Round 3: what we know
- What has the client told you so far? Paste notes or summarise.
- What do you already believe about them that we should test?
- Which competitors did they name?
- Anything we should not use or look at?

Round 4: the workshop
- Has the growth workshop happened? If yes, the board link.

## After the last round
1. Write every answer into agent/research-brief.md. Blank stays blank.
2. Replace CLIENT_NAME with the client name in agent/, human/, and research/. Never touch examples/.
3. If a workshop link was given: read the board and put its output into agent/icp.yaml, buying-committee.yaml, triggers.yaml, journey.yaml, site-plan.yaml, and the enemy/pov fields in brand-positioning.yaml, all as status: hypothesis. Translate to English, keep exact quotes in the original language with a translation.
4. Show a short summary: what is filled, what is blank.
5. Offer the next step:
   - No workshop yet: "Want me to run the research pass before the workshop?"
   - Workshop done: "Want me to run the research pass after the workshop?"
