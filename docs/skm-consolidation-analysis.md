# SKM Consolidatie Analyse

**Status:** Sprint 2 - werk in uitvoering
**Doel:** kandidaten identificeren voor template consolidatie via Jinja inheritance, gebaseerd op de inventaris uit Sprint 0 en de gemigreerde templates uit Sprint 1.

## Werkwijze

Per producfamilie kijken we naar:

1. Welke templates zijn er per SKM/variant?
2. Hoeveel verschillen er substantieel (block content)?
3. Hoeveel verschillen er enkel cosmetisch (titel, codes)?
4. Welke kunnen via overerving worden samengetrokken?

## Producfamilies en kandidaten

### Generic familie (Generic, Generic21, Generic23, Generic44)

- Generic = basis empty_letter, av, eid (Sprint 1 al gedaan)
- Generic21, Generic23, Generic44 = boutique varianten met eigen pakketstructuur
- **Voorstel:** Generic blijft de echte basis. Generic21/23/44 worden aliases die enkel coverpage en pakket-block overriden.

### HypoSelect / NewHyp / Investeringskrediet

- ESIS al geconsolideerd in Sprint 1 (HypoSelect extends NewHyp).
- Loan_schedule include is gedeeld via NewHyp/includes/loan_schedule.html.
- **Open vraag voor Erwin:** zijn er Investeringskrediet-specifieke schedule kolommen die we niet uit NewHyp kunnen herleiden?

### Boutique_23 / Boutique_44

- Beide hebben eigen REGData/SIData structuur (~60 paren elk).
- REGData/SIData templates zijn cosmetisch zo goed als identiek tussen 23 en 44.
- **Voorstel:** een gedeelde include directory boutique/REGData/ en boutique/SIData/ met overrides waar nodig.

### Life_Insurance / Credit_Insurance / Short_Term_Cover

- AV Sprint 1 deelt al via Generic.
- Account_movements al geconsolideerd: Boutique_23 extends Life_Insurance.
- **Voorstel:** Short_Term_Cover migreren naar dezelfde basis als Life_Insurance.

## Open vragen voor afstemming Erwin

1. Welke SKM-varianten hebben echt verschillende juridische tekst en welke verschillen alleen op codes en branding?
2. Zijn de REGData/SIData ng_xxx codes deelbaar over Boutique_23 en Boutique_44 of moet elke SKM zijn eigen reeks behouden?
3. Mag Generic21/23/44 als alias verdwijnen ten gunste van Generic + variantblock, of vereisen klanten een eigen mapnaam per SKM?

## Eerste consolidatie-targets (ruwe schatting)

| Templategroep | Voor | Na | Reductie |
|---------------|------|----|----------|
| Boutique REGData/SIData | ~120 bestanden | ~60 bestanden | 50% |
| Generic varianten | 4 mappen | 1 map met varianten | 75% |
| Notification wrappers | 20+ | ~8 | 60% |

Definitieve cijfers volgen na afstemming met Erwin en de eerste rendering tests.
