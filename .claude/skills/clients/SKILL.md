---
name: clients
description: List client projects or download one to this computer. Use when the user says "get client <name>", "open client <name>", "which clients are there", or "list clients".
---

# Clients

Client projects are private repos in the Ish-Development GitHub organisation.

## List clients
Run: gh repo list Ish-Development --topic client-kit --limit 100 --json name,updatedAt
Only repos tagged client-kit are client projects. Other repos in the organisation are not. Show names and when each was last updated, newest first.

## Get a client
1. Find the parent folder of client-template. Clients sit next to it.
2. If a folder with that name already exists there, say:
   "You already have <name>. Open that folder in Claude. It gets the latest version when it opens."
3. Otherwise run from the parent folder: gh repo clone Ish-Development/<name>
4. Say: "Done. Open the <name> folder in Claude."

If the name does not match a client-kit repo, list the clients and ask which one.
Never download repos that are not tagged client-kit.
