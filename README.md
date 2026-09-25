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
Research, brand, and design loop. Start with research, go back whenever you need to.

  research  <->  brand fill  <->  site plan  <->  copy  <->  design / build  ->  growth

- Kickoff: open the client folder in Claude and say "let's go". Claude asks the brief questions.
- Research: runs twice. A light pass before the workshop to prepare it, a deep pass after to test it.
- Brand fill: ask for after_research_brand_fill. It updates /agent from /research.
- Design / copy: ask for homepage, product_page, ads_or_social, support_copy, or ui_or_landing_build.
- Copy: we write it with Compound Writing (installed for everyone through project settings),
  or the client writes it from a wireframe and a Google Doc ("copy brief").
- Growth: after launch, once a quarter, say "growth review". Claude reads Webflow Analyze,
  asks for a Search Console export, and recommends the next sprints.

When to loop back
- The AI flags a conflict between research and /agent (logged in research/08-risks-and-questions.md).
- A client answer changes one of the 5 key unknowns.
- The client adds a new industry. Steps are in agent/icp.yaml.
- Design work shows a claim or audience assumption that no source supports.
After new research, run brand fill again before more design work.

Example prompts
- "Using only the files in /agent, write homepage hero copy and a 3-section landing page in the brand voice."
- "Plan the site structure from the workshop, one job per page."
- "Build the contact page using site-plan.yaml and section-library.md."
