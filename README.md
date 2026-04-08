# Templating & Compliance  - vFinance Document Templates

## Project Overview

Dit project richt zich op de modernisering van het documenttemplate-beheer voor vFinance, het documentgeneratiesysteem van Patronale Life NV. Het doel is om compliance-risico's te verminderen, duplicaten te consolideren, en het volledige lifecycle-beheer van templates te automatiseren.

### Probleemstelling

1. **Compliance-risico**: Wettelijke documenten (ESIS, AV, EID) bevatten mogelijk verouderde juridische inhoud
2. **Duplicaten & fragmentatie**: Elke SKM heeft eigen mappen met bijna identieke templates
3. **Geen versiebeheer**: Geen controle over welke templates in gebruik zijn per vFinance-versie
4. **Lifecycle gaps**: Templates moeten werken in Feature Freeze, Stable en Release builds
5. **Handmatige JSM-intake**: Minimale automatisering bij template-wijzigingsverzoeken

### Doelstellingen

- Migratie van visuele XML-templates naar Jinja HTML
- Deduplicatie en normalisatie via Jinja inheritance
- Template Registry (JSON) met SKM ↔ template key ↔ semver ↔ lifecycle
- Compatibiliteitsmatrix per vFinance-vintage
- Git-branchingworkflow per lifecycle (feature-freeze → stable → release)
- JSM-automatisering via GitHub Actions
- CI-pipeline voor template-validatie
- Handoverdocumentatie

## Repository Structure

```
templates/
├── _shared/                  # Shared Jinja macros and helpers
├── base/                     # Base XML templates (DOCX pipeline)
├── documents/                # Product-specific document templates
│   ├── Boutique_23/          # Including REGData/ and SIData/
│   ├── Credit_Insurance/
│   ├── Generic/
│   ├── GenericLoan/
│   ├── HypoSelect/
│   ├── Life_Insurance/
│   ├── NewHyp/
│   ├── Wet4892/
│   └── ... (23 product lines)
├── includes/                 # Shared includes (html_head, recipient, signatures)
├── notifications/            # Notification wrappers per product
├── partials/                 # Reusable partial templates
├── images/                   # Logos and branding assets
└── installation_templates/   # Reference templates (vintage 1210)

.github/workflows/            # GitHub Actions (CI, JSM sync)
config/                       # Configuration files
scripts/                      # Automation scripts
docs/                         # Project documentation
```

## vFinance Versioning Model

Templates worden beheerd per vFinance-versie via **vintage branches**:

- **`vintage_1074`**  - Huidige actieve branch. Alle moderne omgevingen (vintage 1074 en later) gebruiken deze branch.
- **`vintage_977`**  - Oudere omgevingen die op een eerdere versie draaien.
- **Regel**: Kies altijd de branch die functioneel het dichtst bij je vFinance-versie ligt, maar **nooit nieuwer** dan je huidige installatie.

Niet elke vFinance-release krijgt een eigen branch  - alleen wanneer templates daadwerkelijk anders zijn.

## Branching Strategy

```
main                          # Production-ready releases
├── vintage_1074              # Current working branch
│   ├── feature-freeze/v1.0   # Locked for testing
│   ├── stable/v1.0           # Validated by stakeholders
│   └── release/v1.0          # Production release
└── vintage_977               # Legacy (pre-vintage environments)
```

## Technology Stack

- **Template engine**: Jinja2 met custom filters (`get_setting`, `format_currency`, `format_date`)
- **Rendering**: HTML → PDF pipeline + DOCX packaging via Office Open XML
- **Deployment**: Git-based, deployed via pull naar netwerkshare
- **CI/CD**: GitHub Actions
- **Project management**: JIRA Service Management + GitHub integration
- **Talen**: Tweetalig NL/FR (Belgische verzekeringscontext)

## Aanpak

Het project is opgezet volgens de **Agile/Scrum**-methodologie:

- **4 sprints** van elk 2 weken (aangepast van oorspronkelijk 7 sprints  - zie Groeiportfolio v0 voor motivatie)
- **Sprint 0**: Foundation  - repo setup, inventaris, registry skeleton, DoR/DoD
- **Sprint 1**: Template migratie  - ESIS, AV, EID, loan schedules naar Jinja HTML
- **Sprint 2**: SKM consolidatie + JSM-automatisering (JIRA↔GitHub sync, daily digest, attachment monitor)
- **Sprint 3**: CI pipeline, documentatie, stakeholder validatie, release

De aanpak is bewust gekozen om **eerst een volledig overzicht** te krijgen van de bestaande templates (inventaris), vervolgens de **prioritaire wettelijke documenten** te migreren, daarna de **operationele workflows** te automatiseren, en ten slotte **kwaliteitscontrole en documentatie** af te ronden.

De oorspronkelijke planning voorzag 7 sprints van 2 weken met 2 werkdagen per week (~210 uur). Door een latere formele startdatum is dit gecomprimeerd naar 4 sprints met 3 werkdagen per week (~200 uur). De scope is ongewijzigd  - enkel de tijdsverdeling is aangepast.

## Documentatie

- `DOCUMENTATION.md` - Technische documentatie (render stack, macro's, filters, extension guide)
- `TEMPLATE_REGISTRY.json` - Template registry met metadata per product
- `COMPAT_MATRIX.md` - Compatibiliteitsmatrix per vFinance-vintage
- `DoR_DoD.md` - Definition of Ready en Definition of Done
- `docs/inventory.md` - Volledige template inventaris (23 productlijnen)
- `docs/versioning-model.md` - vFinance vintage branching documentatie

## Contact

- **Student**: Zacharia Janssen - Zacharia.Janssen@student.vives.be
- **Opdrachtgever**: Patronale Life NV, IT-afdeling
- **Stagebegeleider**: Dirk Hostens - dirk.hostens@vives.be
