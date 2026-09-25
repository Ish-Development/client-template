# Client Template

The starting kit for every Ish client project: research, positioning, site plan, voice, copy, visual identity, QA, and growth, run with Claude.

You talk to Claude in plain words. Claude asks the questions, does the research, drafts, checks, and keeps everything in the right file. You and the client decide.

```text
new client  →  let's go  →  research  →  workshop  →  positioning  →  site plan
            →  tone of voice  →  copy  →  visual identity  →  design QA  →  growth
```

Works in Claude Code, in the terminal or the desktop app.

---

## Start here

**New client**

1. Open the `client-template` folder in Claude.
2. Say: `new client "Client name"`
3. Claude creates the client's own private repo and downloads it next to the template.
4. Open the new client folder in Claude and say: `let's go`

**A client a colleague started**

1. Open the `client-template` folder in Claude.
2. Say: `get client "Client name"`
3. Open that client folder in Claude.

First time on this computer? Do the [one-time setup](#one-time-setup) first.

---

## How it works

### Words first

The site plan and the copy come before high-fidelity design, so the design is built around real words, not lorem ipsum.

### It moves like a spine

Every step can move the others. Start with research, and go back whenever you need to. Most of the back-and-forth happens when the client sees design and copy together. Nothing here is a one-way gate.

### Claude drafts, people decide

Claude researches, drafts, checks, and asks. It never makes a brand decision on its own, never invents facts, and builds nothing. Designers design, the team builds, the client approves.

**Designers:** read [DESIGNERS.md](DESIGNERS.md) for how to set up hi-fi and motion, and where to save your files.

---

## The workflow

| # | Step | What happens | Who decides | Say |
|---|---|---|---|---|
| 1 | Kickoff | Claude asks the brief questions, a few at a time | You | `let's go` |
| 2 | Research, light | Company, market, competitors, current site, SEO and AEO audit | Claude, you check | yes when offered |
| 3 | Workshop | Run the growth workshop. Claude reads the board into the kit | You and the client | `workshop done` + board link |
| 4 | Research, deep | Tests what the workshop said against the outside world | Claude, you check | yes when offered |
| 5 | Positioning | Who it's for, category, enemy, POV, one-liner | You, then the client signs off | `positioning` |
| 6 | Site plan | Every page gets one job. Sitemap and wireframe for the client | You, then the client signs off | `site plan` |
| 7 | Tone of voice | VOICE.md and STYLE.md, built with Compound Writing | You (internal) | `tone of voice` |
| 8 | Copy | Copy for any part of the wireframe, or Google Docs for the client | You | `write copy for the home hero` |
| 9 | Visual identity | Claude collects the designers' work into the kit | Designers | send the design sources |
| 10 | Design QA | Critique in Figma, read-only QA of the Webflow site | Designers, the team | `design critique`, `QA the site` |
| 11 | Growth | Quarterly review of the live site's data | You and the client | `growth review` |

**At any time**

| Say | What happens |
|---|---|
| `client feedback` + paste it | Claude sorts each point to the step it belongs to and asks before changing anything |
| `save my work` | Claude shows what changed, asks, then saves to GitHub |
| `get client "Client name"` | Downloads a client someone else started |
| `which clients are there?` | Lists all client projects |
| `update the kit` | Brings template improvements into an older client |

---

## The steps

### 1. Kickoff

Open the client folder and say `let's go`. Claude asks four short rounds of questions: the basics, the company, what you already know, and the workshop. "Don't know" is always a fine answer. Blank stays blank.

Claude then writes `agent/research-brief.md`, puts the client's name in every file, creates the client's folder in Google Drive, and offers the first research pass.

### 2. Research, light (before the workshop)

Claude searches public sources: the client's site, founders, press, job posts, reviews, and the top competitors. It reads what a buyer would read and uses a real browser when a site needs one.

It also runs an **SEO and AEO audit**: can people find the site on Google, and can AI tools like ChatGPT read and recommend it? One part is done with you in the chat: Claude gives you buyer questions one at a time, you ask them in ChatGPT and Google, and paste the answers back.

**You get**
- `research/00` to `04`, `07` (current site), `08`, `09`, and `sources.md`
- Questions to ask in the workshop
- `human/what-we-found.md`: a one-page summary to show the client

Every claim is marked as fact or inference, with a confidence level and a source.

### 3. Workshop

Run the growth workshop in FigJam with the client. Then say `workshop done` and paste the board link.

Claude reads each block (ICP, buying committee, triggers, category, enemy, POV, bow tie, page jobs) into the matching file as a **hypothesis**. It skips template examples and instructions, translates to English, and keeps exact quotes in the original language.

It tells you what was empty (the Blocker column always gets flagged), where the board disagrees with itself, and where it disagrees with the research.

### 4. Research, deep (after the workshop)

Claude tests what the client said against the evidence. Who is really quoted in their case studies? What do buyers actually search for? It always looks for blockers.

Before it starts, Claude asks two things:
- Should we add customer interviews? It writes the interview guide and analyses the notes.
- Deep on every industry, or only the main one for now?

Research only reports. It never changes the brand files. That happens in positioning.

### 5. Positioning

Say `positioning`. Claude goes through it in a fixed order:

1. **Agreements.** Where the workshop and research agree, it marks them as validated.
2. **Decisions, one at a time.** Where they disagree, you see both sides and the source, and choose.
3. **Core lines.** Three options each for the one-liner, the difference, and the POV. You pick or edit.
4. **Client sign-off.** `human/positioning-summary.md`, one page in plain words.

### 6. Site plan

Say `site plan`. We organise the site by the **job each page does**, not by subject:

| Job | What it does |
|---|---|
| Converter | Turns interest into a conversation: forms, booking, contact |
| Collector | Keeps people who are not ready yet, with an email |
| Attractor | Catches people who were not looking: campaigns, launches, events |
| Informer | Answers what a buyer must settle before choosing |

Every page gets one job, one next action, how it's measured, its URL, and the search question it answers.

**You get** `sitemap/index.html`: one black and white HTML file with the whole information architecture and a clickable wireframe for every page. Send it to the client to sign off.

### 7. Tone of voice

Say `tone of voice`. Built on [Compound Writing](https://github.com/EveryInc/compound-writing).

- **The client has a voice worth keeping:** Claude learns it from their own writing.
- **No voice yet:** give Claude 2 to 5 websites you like. It writes three voice directions with the same sample lines in each. You pick or mix.

Claude then builds `agent/VOICE.md` (how it sounds) and `agent/STYLE.md` (what the copy must do), and tests the voice on a real section. You edit.

Tone of voice stays internal. The client reacts to it when they see design and copy together.

### 8. Copy

**We write it.** Point at any part of the wireframe: `write copy for the home hero`, `section 3 on the product page`, `all of the contact page`. Claude writes it with Compound Writing, gives three headline options, checks voice, AI tells, and claims, and puts the copy in the wireframe box.

**The client writes it.** Say `copy brief`. Claude makes a Google Doc for every page, with guidance for every section in plain words, and links each Doc from the sitemap. Nothing is shared until you share it.

### 9. Visual identity

Designers design it, anywhere: Figma, HTML files, code, PDFs, a live site. Send the links or drop files in `human/visual-sources/`.

Claude reads every source, including motion, and organises it in `agent/visual/`:

| File | What it is |
|---|---|
| `tokens.json` | Colors, type, radius, space |
| `motion.json` | Easing and durations |
| `usage.md` | How to use it, plus the designers' hard rules |
| `components.html` | Real components, when designers deliver them |
| `icons/`, `logo.svg` | SVG, never PNG |
| `demos/` | Working HTML pages from designers |

Claude never invents or changes a value. When two sources disagree, it asks.

How designers set up Figma, motion, and components, and where to save files: [DESIGNERS.md](DESIGNERS.md).

### 10. Design critique and QA

Claude builds nothing. It checks.

- **`design critique`** + a Figma link. Claude checks the design against the kit: tokens, sections, copy, consistency, accessibility. Small misses, like a forgotten border radius or off-scale spacing, it fixes only after the designer says yes. Bigger things are critique only.
- **`QA the site`.** Claude inspects the Webflow site read-only, at mobile, tablet, and desktop, and writes a ranked issue list in `qa/`. The team fixes.

### 11. Growth

After launch, once a quarter, say `growth review`. Claude reads Webflow Analyze, asks you for a Search Console export, and checks every page against its job. It finds where visitors drop off, re-runs the AI questions, plans Webflow Optimize tests, and writes `growth/YYYY-QN.md` with fixes ranked by impact. Real numbers only.

---

## Working together

**Always the latest version.** Every time you open a project, Claude gets the latest version from GitHub first.

**Saving.** Say `save my work`. Claude shows what changed and asks before saving. If a colleague changed the same file, it stops, shows both versions, and asks which to keep. It never overwrites someone's work.

**Improving the kit.** Change the kit in `client-template` and save it. Every new client gets the change. An existing client keeps its version until someone says `update the kit` in that client's folder. Claude then shows what changed and asks first. Client content is never replaced.

**Never fill in the template itself.** Client work always happens in the client's own folder.

**Google Drive for the client.** Every client gets a folder inside the [Ish Drive folder](https://drive.google.com/drive/folders/0ABw6YFhCn2x9Uk9PVA), created at kickoff. Only what the client reads goes there, as Google Docs:

| Doc | When |
|---|---|
| What we found | After the light research |
| Positioning summary | For positioning sign-off |
| Website copy (a Doc per page) | When the client writes the copy |

Nothing is shared automatically. You decide who gets access. When the client comments in a Doc, say `client feedback` and Claude reads the comments.

---

## What lives where

```text
client-template/
├── CLAUDE.md            The rules Claude follows. Loaded automatically.
├── DESIGNERS.md         How designers work with the kit
├── agent/               The brand system, in forms Claude can use
│   ├── research-brief.md    Filled at kickoff
│   ├── research-agent.md    How research is done
│   ├── icp.yaml             Ideal customer
│   ├── buying-committee.yaml  Champion, influencer, blocker, decision maker
│   ├── triggers.yaml        Events that start a purchase
│   ├── journey.yaml         Bow tie stages
│   ├── brand-positioning.yaml
│   ├── brand-values.yaml
│   ├── site-jobs.md         The four jobs
│   ├── section-library.md   Sections by job
│   ├── site-plan.yaml       Every page, its job, its sections
│   ├── VOICE.md             How it sounds
│   ├── STYLE.md             What the copy must do
│   ├── constraints-messaging.yaml  Hard rules for claims and words
│   ├── visual/              Tokens, motion, usage, components, SVGs, demos
│   └── retrieval-rules.yaml Which files each task reads
├── research/            Evidence. 00 overview to 09 SEO and AEO, plus sources
├── sitemap/             The HTML sitemap and wireframe for the client
├── copy/                Copy drafts per page, voice examples, feedback log
├── qa/                  Design critiques and QA reports
├── growth/              Quarterly growth reviews
├── human/               For people: client summaries, PDFs, screenshots, raw design sources
│   └── visual-sources/      Designers drop files here (see DESIGNERS.md)
└── examples/            A fictional sleep brand, fully filled. Reference only.
```

**`/agent` is for Claude. `/human` is for people.** Final client PDFs, Figma screenshots, moodboard images, and long strategy essays stay in `/human`.

---

## Rules Claude follows

The full rules are in [`CLAUDE.md`](CLAUDE.md). In short:

- **No invented facts.** No made-up quotes, numbers, customers, or traction. Unknown stays Unknown, with a question.
- **Facts and inference are labelled**, with a confidence level and a source.
- **Research is evidence, the brand files are decisions.** When they disagree, Claude follows the brand files, flags the conflict, and you decide.
- **When files conflict:** the hard rules win, then positioning, then values, then voice.
- **Everything is written in English.** Quotes in other languages stay original, with a translation.
- **Public pages only.** Claude never logs in to any site, and never gets around a paywall or block.
- **Claude asks before saving to GitHub**, and before any fix in Figma.
- **Claude builds nothing** in Figma or Webflow.

---

## One-time setup

Once per person, per computer. Claude does it for you.

1. **Install Claude Code**, the desktop app or the terminal version.
2. **Open Claude in the folder where you keep your projects**, and paste this:

```text
Set me up for the Ish client template.
1. Check if Node.js (LTS) and the GitHub CLI (gh) are installed. Install what is missing.
2. Log me in to GitHub with gh. I will approve it in the browser.
3. Check I have access to the Ish-Development organisation.
4. Download the template here: gh repo clone Ish-Development/client-template
5. Check which of these Claude can reach: Figma, Webflow, Google Drive. For each one
   that is missing, walk me through connecting it, then test that it works.
6. Tell me in plain words what you did, and what I need to do next.
```

3. **Approve the GitHub login** in your browser when Claude asks. If Claude asks you to type a command yourself, type it with `!` in front, like `! gh auth login`.
4. **Open the new `client-template` folder in Claude.** Accept when Claude Code asks to install the Compound Writing plugin.
5. **Connect Figma, Webflow, and Google Drive.** Claude walks you through it and tests each one.
   You click approve in the browser. For Webflow and Google Drive that happens in Claude's
   settings under Connectors; Claude gives you the link.

| Connector | Needed for |
|---|---|
| Figma | Reading the workshop board, design sources, design critique |
| Webflow | Visual sources, site QA, growth review |
| Google Drive | The client's folder: What we found, Positioning summary, copy Docs |

**Optional:** a free Google PageSpeed API key makes speed checks reliable. Ask Claude: `help me add a PageSpeed API key as PSI_API_KEY`.

Each client folder installs its own research browser the first time you say `let's go`. You don't need to do anything.

<details>
<summary>Prefer to do it by hand?</summary>

1. Install Node.js from [nodejs.org](https://nodejs.org). Pick the LTS version.
2. Install the GitHub CLI from [cli.github.com](https://cli.github.com).
3. In the terminal, run `gh auth login`, choose GitHub.com, and log in with the browser.
4. In your projects folder, run `gh repo clone Ish-Development/client-template`.

</details>

---

## Tools inside the kit

| Tool | What it does | How it gets there |
|---|---|---|
| [Compound Writing](https://github.com/EveryInc/compound-writing) | Voice, style, drafting, and checks for all copy | Project settings ask you to install it |
| [agent-browser](https://github.com/vercel-labs/agent-browser) | A real browser for research, screenshots, and QA | `npm run setup`, run for you at kickoff |
| Figma | Reads FigJam and Figma files | Project settings ask you to install it, Claude helps you log in |
| Webflow connector | Reads Webflow sites and Analyze data | Claude's Connectors settings, Claude helps |
| Google Drive connector | The client's folder and Docs, reads client comments | Claude's Connectors settings, Claude helps |
| GitHub CLI | Creates, downloads, and saves client repos | One-time setup |

---

## Skills

Skills are Claude's instructions for each step. You don't need to name them. Say what you want and Claude picks the right one.

| Skill | Step | Say |
|---|---|---|
| `kickoff` | New client, 1 | `new client "Client name"`, `let's go` |
| `workshop` | 3 | `workshop done` |
| `positioning` | 5 | `positioning` |
| `site-plan` | 6 | `site plan`, `sitemap` |
| `tone-of-voice` | 7 | `tone of voice` |
| `copy` | 8 | `write copy for …` |
| `copy-brief` | 8 | `copy brief` |
| `visual-identity` | 9 | `visual identity` |
| `design-qa` | 10 | `design critique`, `QA the site` |
| `growth-review` | 11 | `growth review` |
| `client-feedback` | Any time | `client feedback` |
| `clients` | Any time | `get client "Client name"`, `which clients are there?` |
| `update-kit` | Any time | `update the kit` |

Research (steps 2 and 4) runs from `agent/research-agent.md`.

---

## Troubleshooting

**"Compound Writing is not installed."** Run `/plugin install compound-writing@compound-writing` in Claude, then start a new session.

**Claude can't read a site, or says "Couldn't access".** The site is blocked or needs a login. Claude won't get around that. Paste the text in yourself.

**Speed shows Unknown.** Google refused the check without a key. Add a PageSpeed API key as `PSI_API_KEY`, or leave it.

**"This is the template."** You said `let's go` in `client-template`. Say `new client "Client name"` there instead, then open the new folder.

**A client doesn't show up in the list.** Only repos tagged `client-kit` are clients. Kickoff tags them automatically. Ask whoever created it to check.

**Claude stopped while saving.** A colleague changed the same file. Claude shows both versions. Pick one, or ask them.

**Claude can't read Figma, Webflow, or Google Drive.** Say `help me connect Figma` (or Webflow, or Google Drive). Claude walks you through it.
