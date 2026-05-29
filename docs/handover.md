# Handover - vFinance Templating & Compliance

Dit document beschrijft hoe het systeem in elkaar zit en hoe je het overneemt
na de stage. Bedoeld voor het vFinance team (Erwin, Eduardo) en een eventuele
opvolger.

## Wat is dit

Een gemoderniseerde set documenttemplates voor vFinance, plus de automatisering
errond. Templates zijn gemigreerd van visuele XML naar Jinja HTML met overerving,
gedocumenteerd in een registry en een compatibiliteitsmatrix, en gekoppeld aan
JIRA Service Management via GitHub Actions.

## Mappen

| Map | Inhoud |
|-----|--------|
| `templates/` | De Jinja templates, per product onder `documents/` |
| `templates/_shared/` en `_shared_boutique/` | Gedeelde base-templates voor overerving |
| `scripts/` | Automatiseringsscripts + de template-validator en generator |
| `.github/workflows/` | De GitHub Actions (CI, JSM sync, digest, monitor) |
| `config/` | Configuratie (JSM sync, fondsenlijst) |
| `docs/` | Documentatie (inventaris, versioning, deze handover, SKM analyse) |

## Een nieuwe template toevoegen

1. Kijk of er een gedeelde base is die past (`_shared/_base_letter`, `_base_document`, of een familie-base zoals `Generic23`).
2. Maak een bestand `documents/<Product>/<type>_<locale>.html` dat de base extend.
3. Overschrijf enkel de blocks die verschillen (titel, document_code, een sectie).
4. Voeg een entry toe in `TEMPLATE_REGISTRY.json` en een rij in `COMPAT_MATRIX.md`.
5. Run `python scripts/validate_templates.py` lokaal. De CI doet dit ook op elke push.

## ng-fiches (REGData/SIData)

De fondsfiches worden niet met de hand gemaakt maar gegenereerd:

1. Voeg het fonds toe aan `config/ng_funds.json`.
2. Run `python scripts/gen_ng_templates.py`. Bestaande bestanden blijven staan.
3. Valideer en commit.

## Automatisering (JSM)

Zie `scripts/README.md` voor de details per workflow. Kort:

- **outbound** - open GIT-ticket wordt een feature branch
- **inbound** - gemergede PR sluit het ticket en zet de template-ticket op Testing Template
- **digest** - dagelijkse tweetalige mail met gewijzigde tickets
- **attachment monitor** - grote bijlagen naar OneDrive (zie open punten)

Secrets staan in de repo settings: `JIRA_USER`, `JIRA_TOKEN`, `GH_PAT`,
`SMTP_USER`, `SMTP_PASS`, `GRAPH_TOKEN`. De transition-ids en ontvangers
staan in `config/jsm_sync.example.json` en moeten mee als het PLVFIN workflow
scheme wijzigt.

## Open punten

- De **attachment monitor** is functioneel klaar (incl. upload session voor
  bestanden > 250MB) maar staat bewust nog NIET live. Hij verwijdert bijlagen
  in productie-JIRA, dus dat zetten we pas aan na expliciete go van Erwin en op
  een eigen service-account ipv een persoonlijk token.
- Voor SIData bestaat voorlopig enkel een NL base; de FR fiches vallen daarop
  terug. Een aparte FR base is nog op te zetten.
- De vintage_977 compatibiliteit is bewust beperkt (zie matrix). Die oude
  vintage is bevroren.
