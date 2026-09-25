# Project rules

This is a brand + web project kit.
Read before writing copy, research, or UI.

Where things live
- /agent: the brand system, in forms Claude can use. Source of truth for all output.
  agent/visual/ holds tokens, usage, components, SVGs, motion, and demos.
- /research: evidence. Research output goes here only.
- /sitemap: the black and white HTML sitemap for the client.
- /copy: page copy drafts, one folder per page.
- /qa: design critiques and internal QA reports.
- /growth: quarterly growth reviews after launch.
- /human: for people. Client PDFs and summaries, Figma screenshots, moodboard images, long
  strategy essays, raw design sources. Not agent source of truth.
- /examples: fictional samples. Never use as client content.

Always
1. Read agent/retrieval-rules.yaml first.
2. Load only the files listed for the current task.
3. If files conflict, use this order:
   constraints-messaging.yaml and the Hard rules in agent/visual/usage.md
   brand-positioning.yaml
   brand-values.yaml
   VOICE.md and STYLE.md
   everything else
4. Do not invent claims, metrics, or product facts.
5. Don't fill in client facts until research or the workshop provides them.
6. Research is evidence, not rules. If research contradicts a file in /agent:
   follow the /agent file, say so in your reply, and add the conflict to
   research/08-risks-and-questions.md. The team decides whether to update /agent.
7. If a file the task needs is still blank, say so. Do not fill the gap with guesses.
8. Write everything in English. Sources and workshop notes may be in other languages:
   translate them, but keep exact quotes in the original language with an English translation next to them.
9. Run the browser as npx agent-browser. If it is missing, run npm run setup.
   When browsing, follow the browsing rules in agent/research-agent.md. Public pages only.
   Never log in, never get around a paywall or block. If blocked, say so and move on.

Tasks, in workflow order
- new project / "let's go": kickoff skill
- research: follow agent/research-agent.md and agent/research-brief.md
- "workshop done" or a workshop board link: workshop skill
- positioning: positioning skill
- site plan / sitemap / information architecture: site-plan skill. Organise by job,
  not by subject (agent/site-jobs.md)
- tone of voice: tone-of-voice skill
- copy, we write it: copy skill. The user points at a part of the wireframe,
  Claude writes it with Compound Writing and shows it in the sitemap.
- copy, the client writes it: copy-brief skill
- visual identity: visual-identity skill. Designers make it (Figma, HTML, code, anything).
  Claude only reads and stores it. Never invent a color, font, timing, or value.
- "design briefing": summarise for a designer, in plain words: the pages and their jobs
  (sitemap), the positioning, how the brand sounds (VOICE.md), and the visual identity so far
  (agent/visual/usage.md). Point to DESIGNERS.md. Read-only.
- design critique / internal QA: design-qa skill. Claude builds nothing. Small Figma fixes
  only after the designer says yes. Webflow is read-only.
- homepage / product page / ads / support / UI: use the matching key in retrieval-rules.yaml
- growth review after launch: growth-review skill
- client feedback, at any time: client-feedback skill
- "update the kit": update-kit skill
- Every page has one job and one next action from agent/site-plan.yaml

Compound Writing's writing home is split across the kit: VOICE.md and STYLE.md in agent/,
examples in copy/examples/, drafts in copy/<page>/. Audience lives in
agent/buying-committee.yaml and agent/icp.yaml, never AUDIENCE.md. Create no other folders.

The process is not linear. It moves like a spine: feedback on one step can move the others,
and any task can send the work back to an earlier step.

Google Drive (for the client)
- Every client gets one folder inside the Ish Drive folder:
  https://drive.google.com/drive/folders/0ABw6YFhCn2x9Uk9PVA
  Named after the client. Its link is in agent/research-brief.md under Google Drive folder.
- Only client-facing documents go there, as Google Docs: What we found, Positioning
  summary, and the Website copy subfolder (copy-brief). Internal files stay in GitHub.
- Never share anything. The user decides who gets access.
- Client comments in these Docs are feedback: read them with comments included and use
  the client-feedback skill.

Saving work
When the user says "save my work" or similar: show a short list of what changed,
ask to confirm, then get the latest (git pull), then commit and push.
Never commit or push without a yes.
If a colleague changed the same file, stop. Show both versions in plain words and
ask which to keep. Never overwrite someone else's work.
Never change the client-template repo from a client folder.

Output
Write into the project. Do not only chat the answer unless asked.
