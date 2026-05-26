# JSM automatisering

Deze map bevat de automatiseringsscripts die via GitHub Actions draaien.
Ze koppelen JIRA Service Management (project PLVFIN) aan deze repo.

Secrets staan in de repo settings (Settings > Secrets and variables > Actions):
`JIRA_USER`, `JIRA_TOKEN`, `GH_PAT`, `SMTP_USER`, `SMTP_PASS`, `GRAPH_TOKEN`.

## Overzicht

| Script | Workflow | Trigger | In | Uit |
|--------|----------|---------|----|----|
| `jsm_sync_outbound.py` | jsm-sync-outbound | elke 5 min | open GIT-tickets | feature branch + ticket op In Progress |
| `jsm_sync_inbound.py` | jsm-sync-inbound | PR merged | gemergede PR | GIT-ticket Done + PLVFIN op Testing Template |
| `daily_digest.py` | daily-digest | werkdag 7u | tickets gewijzigd < 24u | NL+FR mail naar team |
| `attachment_monitor.py` | attachment-monitor | elke 30 min | bijlagen > 400MB | OneDrive upload + share-link in comment |

## Outbound sync

Zoekt GIT-tickets in status Open, leidt de vintage branch af uit het label
(default `vintage_1074`), en maakt `feature/<KEY>-<slug>`. Config voor de
status- en vintage-mapping staat in `config/jsm_sync.example.json`.

## Inbound sync

Leest de GIT-ticketkey uit de branchnaam van de gemergede PR. Zet het ticket
op Done en de gelinkte template-ticket op Testing Template. Als er geen
ticketkey in de branchnaam zit stopt het script gewoon.

## Daily digest

Tweetalige (NL boven, FR onder) mail. Mail-templates in `email_templates/`
gebruiken inline styles + MSO conditional comments zodat Outlook desktop
de tabel correct rendert. Zonder SMTP creds draait het script in dry-run.

## Attachment monitor

Bijlagen boven 400MB breken de Backbone sync naar Vortex. De monitor uploadt
ze naar OneDrive (Graph API), zet een share-link in een ticket-comment en
verwijdert de oorspronkelijke bijlage.

> Let op: bestanden > 250MB hebben een Graph upload session nodig. Dat staat
> nog als TODO in het script, voorlopig getest met bestanden net boven 400MB
> via gewone PUT (werkt tot de Graph limiet).
