# Project rules

This is a brand + web project kit.
Read before writing copy, research, or UI.

Where things live
- /agent: the brand system. Source of truth for all output.
- /research: evidence. Research output goes here only.
- /sitemap: the black and white HTML sitemap for the client.
- /copy: page copy drafts, one folder per page.
- /growth: quarterly growth reviews after launch.
- /human: reference for designers and clients. Not agent source of truth.
- /examples: fictional samples. Never use as client content.

Always
1. Read agent/retrieval-rules.yaml first.
2. Load only the files listed for the current task.
3. If files conflict, use this order:
   constraints-*.yaml
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

Tasks
- new project / "let's go": use the kickoff skill
- "update the kit": use the update-kit skill
- copy, we write it: use Compound Writing (cw-scribe). Voice and style: agent/VOICE.md and
  agent/STYLE.md. Drafts: copy/<page>/. See copy/README.md
- copy, the client writes it: use the copy-brief skill
- growth review after launch: use the growth-review skill
- research: follow agent/research-agent.md and agent/research-brief.md
- "workshop done" or a workshop board link: use the workshop skill
- positioning: use the positioning skill
- tone of voice: use tone_of_voice. Claude drafts VOICE.md and STYLE.md from research,
  the team edits. Use Compound Writing skills (cw-voice-check, cw-save) to refine.
- visual identity: use visual_identity. Designers create it in Figma. Claude only reads it:
  colors, type, spacing from Figma variables and styles into visual-system.json, rules into
  constraints-visual.yaml. Never invent a color, font, or value. Website-only projects:
  import the client's existing brand guidelines (PDF or Figma) the same way.
- site plan / sitemap / information architecture: use the site-plan skill. Organise by job,
  not by subject (agent/site-jobs.md)
- homepage / product page / ads / support / UI: use the matching key in retrieval-rules.yaml
- Every page has one job and one next action from agent/site-plan.yaml

The process is not linear. Any task can send the work back to research.

Saving work
When the user says "save my work" or similar: show a short list of what changed,
ask to confirm, then get the latest (git pull), then commit and push.
Never commit or push without a yes.
If a colleague changed the same file, stop. Show both versions in plain words and
ask which to keep. Never overwrite someone else's work.
Never change the client-template repo from a client folder.

Output
Write into the project. Do not only chat the answer unless asked.
