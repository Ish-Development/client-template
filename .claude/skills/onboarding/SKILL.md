---
name: onboarding
description: Bring a colleague up to speed on the project at project-manager level, in one page. Use when the user says "onboard me", "onboarding", "give me a summary", "where are we", "catch me up", or a colleague (e.g. the project manager) is starting on the project.
---

# Onboarding

For a colleague who needs the big picture, not the details. Think project manager:
what we are building and why, how far we are, what changed lately, what we wait for,
what could go wrong, and what happens next. One page they can read in five minutes.

Read-only. Change nothing unless the user asks you to save the brief (step 4).

## 1. Read, in this order
1. The newest status file in human/ (human/YYYY-MM-DD-*status*.md). It is the starting point.
2. What changed after its date:
   `git log --since=<status date> --format="%ad %s" --date=short`
   The commit messages say the decision and why. Also the entries after that date in
   any dated log in qa/ (e.g. a Figma sections log).
3. The project itself, only if the status file doesn't cover it:
   agent/research-brief.md (client, goal, scope, Drive folder), human/positioning-summary.md,
   agent/site-plan.yaml (pages and their jobs).
4. Open questions and risks: research/08-risks-and-questions.md. Only the open ones.

Do not read component, token or copy files. A project manager doesn't need them.

## 2. Work out where we are in the workflow
Use the task list in CLAUDE.md ("Tasks, in workflow order") as the steps:
kickoff, research, workshop, positioning, site plan, tone of voice, copy, visual identity,
design QA, build, growth review. Mark each one done, in progress or not started, with the
evidence (a file, a commit, a status note). If you can't tell, say "unclear", don't guess.
The process is not linear: a step marked done can be reopened by feedback. Say so when it happened.

## 3. Write the brief
Plain words, short paragraphs, no file paths except in "Where to look".
Group changes by decision, not by file or by day. Leave out Figma component details,
variable names, copy wording and draft numbers.

```
# <Client>: where we are (<date>)

## The project in short
2–3 sentences: who the client is, what we are building, the goal, what's in Phase 1.

## Where we are
The workflow steps, one line each: done / in progress / not started.

## What changed since <status date>
3–7 bullets. Each: the decision and why.

## Waiting on the client
Open questions that block or slow work. Who on the client side, if known.

## Risks and parked decisions
Only what a PM should track. Say which are assumptions.

## Next
The next 3–5 steps, with who owns them (by role or name, as the status files do).

## Where to look
Sitemap (sitemap/index.html), the Figma file, the client's Drive folder, the newest status file.
```

Never invent dates, owners, numbers or deadlines. If the files don't say, write "not known"
and list it under a short "Ask the team" line at the end.

## 4. Offer to save it
Ask whether to save the brief as human/<today>-status.md. If yes, it becomes the newest
status file, so the next onboarding starts from it. Then offer "save my work".
