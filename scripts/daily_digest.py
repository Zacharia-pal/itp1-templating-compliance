#!/usr/bin/env python3
# Dagelijkse digest van gewijzigde template-tickets, tweetalig NL/FR.
# Draait elke werkdag om 7u via de daily-digest workflow.
#
# Haalt alle PLVFIN tickets op die in de laatste 24u gewijzigd zijn en
# stuurt een nette mail naar het team. Outlook desktop is lastig met CSS,
# dus de mail-template gebruikt inline styles + MSO conditional comments.

import os
import sys
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
from jinja2 import Environment, FileSystemLoader


def load_config(path="config/jsm_sync.example.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

JIRA = "https://patronale.atlassian.net"
JIRA_USER = os.environ.get("JIRA_USER", "zacharia.janssen@patronale-life.be")
JIRA_TOKEN = os.environ.get("JIRA_TOKEN")

SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.office365.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASS = os.environ.get("SMTP_PASS")

JQL = ('project = PLVFIN AND issuetype in ("VF Bug", "GIT", "New Feature") '
       'AND updated >= -1d ORDER BY updated DESC')


def fetch_changed():
    r = requests.get(
        JIRA + "/rest/api/3/search",
        params={"jql": JQL, "fields": "summary,status,assignee,issuetype,updated"},
        auth=(JIRA_USER, JIRA_TOKEN),
        timeout=30,
    )
    r.raise_for_status()
    rows = []
    for it in r.json().get("issues", []):
        f = it["fields"]
        assignee = f.get("assignee") or {}
        rows.append({
            "key": it["key"],
            "summary": f["summary"],
            "status": f["status"]["name"],
            "type": f["issuetype"]["name"],
            "assignee": assignee.get("displayName", "-"),
            "url": JIRA + "/browse/" + it["key"],
        })
    return rows


def render(lang, rows):
    env = Environment(loader=FileSystemLoader("scripts/email_templates"))
    tpl = env.get_template("digest_%s.html" % lang)
    return tpl.render(rows=rows, count=len(rows))


def send(rows, recipients):
    if not SMTP_USER or not SMTP_PASS:
        print("geen SMTP creds, dry-run. %d tickets in digest." % len(rows))
        print(render("nl", rows)[:300])
        return

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "vFinance template digest / %d wijzigingen" % len(rows)
    msg["From"] = SMTP_USER
    msg["To"] = ", ".join(recipients)
    # NL + FR in 1 mail, NL eerst
    body = render("nl", rows) + "<hr/>" + render("fr", rows)
    msg.attach(MIMEText(body, "html", "utf-8"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        s.starttls()
        s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(SMTP_USER, recipients, msg.as_string())
    print("digest verstuurd naar", recipients)


def main():
    if not JIRA_TOKEN:
        print("JIRA_TOKEN ontbreekt")
        sys.exit(1)
    cfg = load_config()
    rows = fetch_changed()
    if not rows:
        print("geen wijzigingen in de laatste 24u, geen mail")
        return
    send(rows, cfg["digest_recipients"])


if __name__ == "__main__":
    main()
