"""Shared helpers for the Jev (TypeSafe) scripts in this folder.

Jev judges; it doesn't write. Each call sends a state and typed questions and gets back
probabilities. Docs: docs.typesafe.ai.
"""
import json, os, re, urllib.request

ROOT = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
API = "https://api.typesafe.ai/v1/systemone"


USER_ENV = os.path.expanduser("~/.ish/.env")  # one key per computer, for every project; outside every repo


def key():
    """JEV_API_KEY from the environment, the project's .env, or ~/.ish/.env (never printed)."""
    if os.environ.get("JEV_API_KEY"):
        return os.environ["JEV_API_KEY"]
    for path in (os.path.join(ROOT, ".env"), USER_ENV):
        try:
            for line in open(path):
                if line.startswith("JEV_API_KEY="):
                    return line.split("=", 1)[1].strip()
        except OSError:
            pass
    return None


def ask(k, state, questions, timeout=25):
    """One request: every question is judged in parallel against the same state."""
    body = {"state": state, "model": "jev-latest", "questions": questions}
    req = urllib.request.Request(API, data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {k}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)["answers"]


def noul(q, true=None, false=None):
    d = {"type": "noul", "instructions": q}
    if true:
        d["criteria"] = {"true": true, "false": false}
    return d


def choice(q, options):
    return {"type": "choice", "instructions": q, "criteria": options}


def score(q, levels):
    return {"type": "score", "instructions": q, "criteria": levels}


def client_name():
    """The client's name from agent/research-brief.md ("Client: ..."), or "the client" before kickoff."""
    try:
        m = re.search(r"^Client: *(.+)$", read("agent/research-brief.md"), re.M)
    except OSError:
        m = None
    name = m.group(1).strip() if m else ""
    return name if name and name != "CLIENT_NAME" else "the client"


def read(rel):
    with open(os.path.join(ROOT, rel)) as f:
        return f.read()



if __name__ == "__main__":  # SessionStart: say so when Jev is off, instead of skipping in silence
    if not key():
        print("Jev is off: no JEV_API_KEY in ~/.ish/.env or the project's .env, so the commit guard, copy review and "
              "task router are skipped. Tell the user once, in plain words. To switch it on: one line "
              "JEV_API_KEY=<key> in ~/.ish/.env (once per computer; never in the project).")
