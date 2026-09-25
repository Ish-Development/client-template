# Client template

The starting kit for every client project. Works in Claude Code: the terminal or the desktop app.

One-time setup (each person, once)
1. Install Node.js: https://nodejs.org (the LTS version).
2. Install the GitHub CLI: https://cli.github.com
3. In the terminal run: gh auth login   (choose GitHub.com, then log in with the browser)
4. Download this template once: gh repo clone Ish-Development/client-template
5. Optional: a free Google PageSpeed API key, saved as PSI_API_KEY, for speed checks.

Start a new client
1. Open the client-template folder in Claude.
2. Say: "new client <name>". Claude creates the client's own repo and downloads it.
3. Open the new client folder in Claude and say: "let's go".
4. To save your work, say: "save my work". Claude asks before saving to GitHub.

Work on a client someone else started
1. Open the client-template folder in Claude.
2. Say: "get client <name>". Claude downloads it once.
3. Open that client folder in Claude.

Always the latest version
Every time you open a project, Claude gets the latest version from GitHub first.
If your unsaved changes clash with a colleague's, Claude stops and asks. It never overwrites.

Kit improvements in older clients
A client keeps the kit version it started with. To bring in later improvements,
open the client folder and say: "update the kit". Claude shows what changed and asks first.
Client content (research, brand files, workshop output) is never replaced.

Never fill in the template itself. Improvements to the kit go into client-template on purpose,
then every new client gets them.

/agent
The brand system. Source of truth for Claude and Figma MCP.
Files start blank. See /examples for a filled sample.

/research
Evidence gathered by the research agent. Feeds /agent.

/copy
Page copy drafts, one folder per page.

/qa
Design critiques and internal QA reports.

/growth
Quarterly growth reviews after launch.

/human
For designers and clients. Figma, PDFs, presentation notes.

/examples
A fictional sleep brand, fully filled. Reference only. Never client content.

CLAUDE.md
Rules Claude follows. Loaded automatically.

Setup (once per client folder)
Kickoff runs this for you: npm run setup
It installs agent-browser (the research browser) and downloads its Chrome.
Everyone gets the same version from package.json.

How we work
The steps move like a spine: each one can move the others. Start with research, go back
whenever you need to. Most back-and-forth happens when the client sees design and copy together.

  research  <->  positioning  <->  site plan  <->  tone of voice  <->  copy
            <->  visual identity  <->  hi-fi design & build  ->  growth

  Words first: the site plan and copy come before high-fidelity design,
  so design is built around real copy.

1. Kickoff: open the client folder in Claude and say "let's go". Claude asks the brief questions.
2. Research, light: before the workshop, to prepare it.
3. Workshop: run the growth workshop in FigJam. Then say "workshop done" with the board link.
   Claude reads each block into /agent as hypotheses and lists what is empty or unclear.
4. Research, deep: after the workshop, to test it.
5. Positioning: say "positioning". Claude validates what research confirms, asks you each
   open decision one at a time, and writes 3 options for the one-liner, difference, and POV.
   Ends with human/positioning-summary.md for the client to sign off.
6. Site plan: say "site plan". Every page gets one job, one next action, one measure, its URL,
   and the search question it answers. Claude builds a black and white HTML sitemap in
   sitemap/index.html: one deliverable with the whole information architecture plus a
   wireframe for every page. Client signs off.
7. Tone of voice: say "tone of voice". Built with Compound Writing. If the client has a voice,
   Claude learns it from their writing. If not, give Claude 2-5 inspiration websites: it writes
   3 voice directions with sample lines, you pick, then it builds VOICE.md and STYLE.md. You edit.
8. Copy: we write it: point at a part of the wireframe ("write copy for the home hero") and
   Claude writes it with Compound Writing (installed for everyone through project settings).
   The copy appears in the wireframe box. Headlines come as 3 options.
   Or the client writes it: Claude makes a Google Doc for every page with guidance for every
   section, linked from the sitemap ("copy brief"). Needs the Google Drive connector.
9. Visual identity: designers design it anywhere: Figma, HTML files, code, PDFs. Give Claude the
   links or drop files in human/visual-sources/. Claude reads each source, including motion,
   and organises them in agent/visual/: tokens, usage, components, SVGs, motion, demos.
10. Hi-fi design & build: designers design, the team builds. Claude builds nothing. Say
    "design critique" with a Figma link: Claude checks it against the kit and fixes small
    things (a missed radius, off-scale spacing) only after the designer says yes.
    Say "QA the site": Claude inspects Webflow read-only and writes a ranked issue list in qa/.
11. Growth: after launch, once a quarter, say "growth review". Claude reads Webflow Analyze,
    asks for a Search Console export, and recommends fixes ranked by impact.

Client feedback
Paste what the client said and say "client feedback". Claude splits it into points, sorts each
to the step it belongs to (voice, positioning, site plan, design, research), shows what would
change, and asks before changing anything. Tone of voice has no separate client sign-off:
the client reacts to it here.

When to loop back
- The AI flags a conflict between research and /agent (logged in research/08-risks-and-questions.md).
- A client answer changes one of the 5 key unknowns.
- The client adds a new industry. Steps are in agent/icp.yaml.
- Design work shows a claim or audience assumption that no source supports.
After new research, run positioning and tone of voice again before more design work.

Example prompts
- "Using only the files in /agent, write homepage hero copy and a 3-section landing page in the brand voice."
- "Plan the site structure from the workshop, one job per page."
- "Build the contact page using site-plan.yaml and section-library.md."
