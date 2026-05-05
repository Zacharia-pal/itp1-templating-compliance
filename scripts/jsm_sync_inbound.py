#!/usr/bin/env python3
# Inbound JSM sync: PR merge -> JIRA terugkoppeling
# Wordt aangeroepen door de jsm-sync-inbound workflow als een PR gemerged is.
#
# Uit de branchnaam (feature/<KEY>-<slug>) halen we de GIT ticketkey.
# Dan: GIT-ticket -> Done, en de gelinkte PLVFIN template-ticket -> Testing Template.

import os
import re
import sys
import requests

JIRA = "https://patronale.atlassian.net"
JIRA_USER = os.environ.get("JIRA_USER", "zacharia.janssen@patronale-life.be")
JIRA_TOKEN = os.environ.get("JIRA_TOKEN")

# transition ids per status (uit het PLVFIN workflow scheme)
TR_DONE = "31"
TR_TESTING = "41"

KEY_RE = re.compile(r"feature/(PLVFIN-\d+)", re.IGNORECASE)


def ticket_from_branch(branch):
    m = KEY_RE.search(branch or "")
    return m.group(1).upper() if m else None


def get_linked_template_ticket(git_key):
    # GIT-ticket heeft een "relates to" link naar het PLVFIN template ticket
    r = requests.get(
        JIRA + "/rest/api/3/issue/%s" % git_key,
        params={"fields": "issuelinks"},
        auth=(JIRA_USER, JIRA_TOKEN),
        timeout=30,
    )
    r.raise_for_status()
    links = r.json()["fields"].get("issuelinks", [])
    for link in links:
        out = link.get("outwardIssue") or link.get("inwardIssue")
        if out and out["key"].startswith("PLVFIN-"):
            return out["key"]
    return None


def transition(key, tid):
    resp = requests.post(
        JIRA + "/rest/api/3/issue/%s/transitions" % key,
        auth=(JIRA_USER, JIRA_TOKEN),
        json={"transition": {"id": tid}},
        timeout=30,
    )
    resp.raise_for_status()


def comment(key, text):
    body = {"body": {"type": "doc", "version": 1, "content": [
        {"type": "paragraph", "content": [{"type": "text", "text": text}]}
    ]}}
    requests.post(
        JIRA + "/rest/api/3/issue/%s/comment" % key,
        auth=(JIRA_USER, JIRA_TOKEN),
        json=body,
        timeout=30,
    ).raise_for_status()


def main():
    branch = os.environ.get("PR_HEAD_REF")
    pr_url = os.environ.get("PR_URL", "")
    if not JIRA_TOKEN:
        print("JIRA_TOKEN ontbreekt")
        sys.exit(1)

    git_key = ticket_from_branch(branch)
    if not git_key:
        print("geen GIT ticket in branchnaam:", branch)
        return  # niks te doen, gewoon stoppen

    print("merge van", branch, "-> ticket", git_key)
    comment(git_key, "PR gemerged: %s" % pr_url)
    transition(git_key, TR_DONE)

    template_key = get_linked_template_ticket(git_key)
    if template_key:
        print("  gelinkt template ticket:", template_key, "-> Testing Template")
        transition(template_key, TR_TESTING)
    else:
        print("  geen gelinkt PLVFIN template ticket gevonden")


if __name__ == "__main__":
    main()
