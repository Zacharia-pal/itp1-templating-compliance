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

## R148 / FF-148 migratie (localization + fixes)

De brieflaag is gemigreerd voor vFinance release 148 (FF-148 -> Release-2):

- **Localization-refactor.** De account_movements-brieven gebruiken 1 unified template
  (`documents/Life_Insurance/account_movements_BE.html`) met de `from_list`-taalselector i.p.v.
  aparte `_nl_BE`/`_fr_BE` bestanden. Life_Insurance is de base; Boutique_23, Generic21/23/44 en
  Short_Term_Cover zijn routers die enkel de titel (en Tak 21 de voet) overschrijven. De
  taalspecifieke tekst zit in taalconditionelen, conform het bestaande codebase-idioom.
  De oude taalbestanden blijven staan tot na de render-test; opkuisen (Fase E) gebeurt pas na
  akkoord van de opdrachtgever.
- **Taal-router.** De dossiertaal komt van de primaire rolhouder (eerste rol), niet van de
  gesorteerd-eerste recipient. Zie `docs/language-router-gotcha.md`.
- **Handtekening-filter.** `convert_custom_image` is in FF-148 verwijderd; de handtekening komt
  nu uit een DB-setting via `get_setting` + `convert_stored_image` (`NOTIFICATION_SIGNATURE`,
  of `HYPO_INVOICE_SIGNATURE` voor hypo-facturen).
- **FR SIData-base.** Er is nu een aparte `sidata_ng_base_fr_BE.html`; de generator kiest per
  locale de juiste base, dus de FR-fiches vallen niet langer terug op de NL-base.
- **CI.** `validate_templates.py` valideert NL en FR en faalt op verwijderde FF-148 filters
  (`convert_custom_image`, `format_role`, `format_asset_feature`, `_get_recipient_data`).

Tak 21-detail: het `movements_footer` block (gewaarborgde rentevoet + premietaks) zat vroeger
niet in de base, waardoor die voet nooit rendorde. Dat block bestaat nu en de voet is tweetalig.

## Open punten

- De **oude `_nl_BE`/`_fr_BE` account_movements-bestanden** staan er nog naast de unified
  templates. Ze mogen weg na een render-test die de unified output bevestigt (Fase E, na go).
- Het unified from_list-patroon is uitgerold op de account_movements-familie. De **overige
  notificaties** volgen hetzelfde patroon maar zijn nog niet allemaal omgezet.
- De **attachment monitor** is functioneel klaar (incl. upload session voor
  bestanden > 250MB) maar staat bewust nog NIET live. Hij verwijdert bijlagen
  in productie-JIRA, dus dat zetten we pas aan na expliciete go van Erwin en op
  een eigen service-account ipv een persoonlijk token.
- De vintage_977 compatibiliteit is bewust beperkt (zie matrix). Die oude
  vintage is bevroren.
