# vFinance Versioning Model

## Overzicht

Het vFinance Sideloader-systeem beheert templates via **vintage branches** in Git. Dit document beschrijft hoe de versioning werkt en hoe de juiste branch gekozen wordt.

## Branch Structuur

```
Production (protected)          ← Productie-branch, niet direct bewerkbaar
├── vintage_1074               ← Huidige actieve branch (alle moderne omgevingen)
├── vintage_977                ← Oudere omgevingen (pre-vintage)
├── Legacy_PROD                ← Transitiebranch met legacy mappen per maatschappij
├── Legacy_DEV                 ← Legacy ontwikkelbranch
└── PLVFIN-XXXX branches       ← Feature branches per JIRA-ticket
```

## Het Vintage Concept

**Niet elke vFinance-release krijgt een eigen branch.** Veel releases bevatten geen template-wijzigingen. Een nieuwe branch wordt alleen aangemaakt wanneer templates daadwerkelijk anders moeten zijn voor een specifieke vFinance-versie.

### Vintage Cutoff: 1074

- Alles **vanaf vintage 1074** gebruikt de branch `vintage_1074`
- Oudere omgevingen blijven op hun bestaande branch (bijv. `vintage_977`)
- Wijzigingen aan deze regel worden expliciet gecommuniceerd

### Branch Selectie Regel

> Kies altijd de branch die functioneel het **dichtst bij** je vFinance-versie ligt, maar **nooit nieuwer** dan je huidige installatie.

**Voorbeeld:**
- vFinance versie 1074 → `vintage_1074` ✓
- vFinance versie 1210 → `vintage_1074` ✓ (geen aparte branch nodig, vintage_1074 werkt)
- vFinance versie 977 → `vintage_977` ✓
- vFinance versie 950 → `vintage_977` ✗ (te nieuw) → zoek oudere branch

## Variabelen per Vintage

Per vFinance-versie kunnen de **beschikbare variabelen** in templates verschillen. Wanneer een nieuwe versie variabelen toevoegt, wijzigt of verwijdert, wordt dit onderzocht en gedocumenteerd. Als de wijzigingen een impact hebben op de templates, wordt een nieuwe vintage branch aangemaakt.

### Voorbeeld van variabele-verschillen:

| Variabele | vintage_977 | vintage_1074 |
|-----------|-------------|--------------|
| `recipient.custom_address` | Niet beschikbaar | Beschikbaar |
| `format_datetime` filter | Beperkte opties | Uitgebreid met timezone support |
| `templates_revision()` | Statisch | Dynamisch uit import |

## Deployment

Templates worden gedeployed via git pull naar een netwerkshare:

```
\\vortex.local\Patronale Life\Program Data\VF_Sideloader_Git\<versie>
```

**Belangrijk:** Altijd het volledige UNC-pad gebruiken, nooit de `W:` drive letter. De W:-letter veroorzaakte historisch problemen met disconnecties en mount-scripts.

### Deploy Stappen

1. Tag versie als `v{X.Y.Z}`
2. Release artifact = zip van template-root
3. Deploy naar netwerkshare (via git pull)
4. Smoke test met fixtures
5. Rollback door vorige zip te herstellen

## vFinance Pad Configuratie

In vFinance zelf worden de template-paden geconfigureerd via:
- vFinance icoon → "Wijzig instellingen" → "V-Finance" tab
- **"Pad met niet-standaard documenten"** → wijst naar installer templates (Vortex-beheerd)
- **"Pad met custom documenten"** → wijst naar `VF_Sideloader_Git/<versie>` (Patronale-beheerd)

## Feature Branches

Voor template-wijzigingen wordt de volgende workflow gevolgd:

1. PLVFIN-ticket aangemaakt in JIRA
2. GIT-ticket wordt automatisch aangemaakt (via git-sync)
3. Feature branch wordt automatisch aangemaakt op basis van `vintage_1074`
4. Ontwikkelaar werkt op de feature branch
5. Pull Request naar `vintage_1074`
6. Na merge: GIT-ticket wordt gesloten, PLVFIN-ticket gaat naar "Testing Template"

## Lifecycle Branches (nieuw, dit project)

Bovenop het vintage model voegen we lifecycle branches toe:

```
vintage_1074
├── feature-freeze/v1.0    ← Gelocked voor testen
├── stable/v1.0            ← Gevalideerd door stakeholders
└── release/v1.0           ← Productie-release
```

Dit maakt het mogelijk om templates te promoten door de levenscyclus heen, met duidelijke gates tussen elke fase.
