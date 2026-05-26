#!/usr/bin/env python3
# Attachment monitor: grote bijlagen (>400MB) verhuizen naar OneDrive.
#
# Backbone sync naar Vortex breekt op hele grote bijlagen. Deze monitor
# zoekt bijlagen boven de limiet, uploadt ze naar OneDrive via Graph,
# en vervangt de bijlage in JIRA door een share-link in een comment.

import os
import sys
import requests

JIRA = "https://patronale.atlassian.net"
JIRA_USER = os.environ.get("JIRA_USER", "zacharia.janssen@patronale-life.be")
JIRA_TOKEN = os.environ.get("JIRA_TOKEN")

GRAPH = "https://graph.microsoft.com/v1.0"
GRAPH_TOKEN = os.environ.get("GRAPH_TOKEN")

LIMIT_BYTES = 400 * 1024 * 1024  # 400 MB
ONEDRIVE_FOLDER = "vFinance-attachments"

JQL = 'project = PLVFIN AND attachments is not EMPTY AND updated >= -1d'


def big_attachments():
    r = requests.get(
        JIRA + "/rest/api/3/search",
        params={"jql": JQL, "fields": "attachment"},
        auth=(JIRA_USER, JIRA_TOKEN),
        timeout=30,
    )
    r.raise_for_status()
    found = []
    for it in r.json().get("issues", []):
        for att in it["fields"].get("attachment", []):
            if att.get("size", 0) > LIMIT_BYTES:
                found.append((it["key"], att))
    return found


def download(att):
    r = requests.get(att["content"], auth=(JIRA_USER, JIRA_TOKEN), timeout=300)
    r.raise_for_status()
    return r.content


SIMPLE_PUT_LIMIT = 250 * 1024 * 1024  # Graph limiet voor een gewone PUT
CHUNK = 10 * 1024 * 1024              # 10MB chunks, moet veelvoud van 320KiB zijn


def upload_to_onedrive(filename, data):
    # tot 250MB kan in 1 PUT, daarboven een upload session met chunks.
    if len(data) <= SIMPLE_PUT_LIMIT:
        url = "%s/me/drive/root:/%s/%s:/content" % (GRAPH, ONEDRIVE_FOLDER, filename)
        r = requests.put(
            url,
            headers={"Authorization": "Bearer " + GRAPH_TOKEN},
            data=data,
            timeout=600,
        )
        r.raise_for_status()
        return create_link(r.json()["id"])
    return upload_session(filename, data)


def upload_session(filename, data):
    # 1. session aanmaken
    create = requests.post(
        "%s/me/drive/root:/%s/%s:/createUploadSession" % (GRAPH, ONEDRIVE_FOLDER, filename),
        headers={"Authorization": "Bearer " + GRAPH_TOKEN},
        json={"item": {"@microsoft.graph.conflictBehavior": "replace"}},
        timeout=30,
    )
    create.raise_for_status()
    upload_url = create.json()["uploadUrl"]  # deze url heeft geen auth header nodig

    total = len(data)
    start = 0
    item = None
    while start < total:
        end = min(start + CHUNK, total)
        chunk = data[start:end]
        headers = {
            "Content-Length": str(len(chunk)),
            "Content-Range": "bytes %d-%d/%d" % (start, end - 1, total),
        }
        r = requests.put(upload_url, headers=headers, data=chunk, timeout=600)
        # 202 = chunk ok meer verwacht, 200/201 = klaar
        if r.status_code in (200, 201):
            item = r.json()
        elif r.status_code != 202:
            r.raise_for_status()
        start = end

    return create_link(item["id"])


def create_link(item_id):
    r = requests.post(
        "%s/me/drive/items/%s/createLink" % (GRAPH, item_id),
        headers={"Authorization": "Bearer " + GRAPH_TOKEN},
        json={"type": "view", "scope": "organization"},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["link"]["webUrl"]


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


def delete_attachment(att_id):
    requests.delete(
        JIRA + "/rest/api/3/attachment/%s" % att_id,
        auth=(JIRA_USER, JIRA_TOKEN),
        timeout=30,
    )  # geen raise, als het al weg is is dat ook ok


def main():
    if not JIRA_TOKEN or not GRAPH_TOKEN:
        print("JIRA_TOKEN of GRAPH_TOKEN ontbreekt")
        sys.exit(1)

    items = big_attachments()
    print("grote bijlagen gevonden:", len(items))
    for key, att in items:
        name = att["filename"]
        mb = att["size"] / 1024 / 1024
        print("-> %s : %s (%.0f MB)" % (key, name, mb))
        data = download(att)
        link = upload_to_onedrive(name, data)
        jira_comment(key, "Bijlage %s (%.0f MB) verplaatst naar OneDrive: %s" % (name, mb, link))
        delete_attachment(att["id"])


if __name__ == "__main__":
    main()
