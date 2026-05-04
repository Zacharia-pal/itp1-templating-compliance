#!/usr/bin/env python3
# Outbound JSM sync: JIRA GIT-ticket -> GitHub feature branch
# Draait elke 5 min via de jsm-sync-outbound workflow.
#
# Flow:
#   1. zoek GIT-tickets in status "Open" zonder branch
#   2. bepaal vintage branch uit het vintage label (default vintage_1074)
#   3. maak feature/<ticketkey>-<slug> branch vanaf die vintage
#   4. zet ticket op "In Progress" en plak de branch-naam in een comment

import os
import sys
import json
import re
import requests

JIRA = "https://patronale.atlassian.net"
JIRA_USER = os.environ.get("JIRA_USER", "zacharia.janssen@patronale-life.be")
JIRA_TOKEN = os.environ.get("JIRA_TOKEN")
GH_TOKEN = os.environ.get("GH_TOKEN")

GH_OWNER = "Zacharia-pal"
GH_REPO = "itp1-templating-compliance"
DEFAULT_VINTAGE = "vintage_1074"


def load_config(path="config/jsm_sync.example.json"):
    # TODO: aparte prod config los van het example bestand
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def jql_search(jql):
    r = requests.get(
        JIRA + "/rest/api/3/search",
        params={"jql": jql, "fields": "summary,labels,status"},
        auth=(JIRA_USER, JIRA_TOKEN),
        timeout=30,
    )
    r.raise_for_status()
    return r.json().get("issues", [])


def slugify(text):
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:40]  # niet te lang anders breekt git ref


def vintage_for(labels, cfg):
    for lbl in labels:
        if lbl in cfg["vintage_labels"]:
            return cfg["vintage_labels"][lbl]
    return DEFAULT_VINTAGE


def gh_get_sha(branch):
    r = requests.get(
        "https://api.github.com/repos/%s/%s/git/ref/heads/%s" % (GH_OWNER, GH_REPO, branch),
        headers={"Authorization": "token " + GH_TOKEN},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["object"]["sha"]


def gh_create_branch(new_branch, from_sha):
    r = requests.post(
        "https://api.github.com/repos/%s/%s/git/refs" % (GH_OWNER, GH_REPO),
        headers={"Authorization": "token " + GH_TOKEN},
        json={"ref": "refs/heads/" + new_branch, "sha": from_sha},
        timeout=30,
    )
    if r.status_code == 422:
        # branch bestaat al, niet erg
        print("  branch bestond al, skip")
        return False
    r.raise_for_status()
    return True


def jira_transition(key, transition_id):
    requests.post(
        JIRA + "/rest/api/3/issue/%s/transitions" % key,
        auth=(JIRA_USER, JIRA_TOKEN),
        json={"transition": {"id": transition_id}},
        timeout=30,
    ).raise_for_status()


def jira_comment(key, text):
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
    if not JIRA_TOKEN or not GH_TOKEN:
        print("JIRA_TOKEN of GH_TOKEN ontbreekt")
        sys.exit(1)

    cfg = load_config()
    jql = 'project = PLVFIN AND issuetype = "GIT" AND status = "Open"'
    issues = jql_search(jql)
    print("gevonden:", len(issues), "open GIT-tickets")

    for issue in issues:
        key = issue["key"]
        summary = issue["fields"]["summary"]
        labels = issue["fields"].get("labels", [])
        vintage = vintage_for(labels, cfg)
        branch = "feature/%s-%s" % (key, slugify(summary))

        print("->", key, "op", vintage, "=>", branch)
        sha = gh_get_sha(vintage)
        created = gh_create_branch(branch, sha)
        if created:
            jira_comment(key, "Feature branch aangemaakt: %s (vanaf %s)" % (branch, vintage))
            # transition id 21 = In Progress (hangt af van workflow scheme)
            jira_transition(key, "21")


if __name__ == "__main__":
    main()
