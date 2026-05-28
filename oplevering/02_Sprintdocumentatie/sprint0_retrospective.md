# Sprint 0 Retrospective

**Sprint:** Sprint 0 - Foundation
**Periode:** 30 maart - 11 april 2026
**Uren gelogd:** ~50h

## Sprint Goal

Repo opzetten, template inventaris maken, registry en compatibiliteitsmatrix skeleton, DoR/DoD definieren, branching model opzetten.

## Wat ging goed

- De inventaris van alle 23 productlijnen was grondiger dan verwacht. Door alles systematisch in kaart te brengen werd meteen duidelijk welke templates kandidaat zijn voor consolidatie.
- Het vintage branching model was goed gedocumenteerd op Confluence, wat het makkelijker maakte om de regels te formaliseren in docs/versioning-model.md.
- De keuze om eerst Generic en GenericLoan als voorbeeld-templates te migreren hielp om het Jinja inheritance patroon uit te testen voor de grotere migratie in Sprint 1.

## Wat kan beter

- Het registry schema moest 2x herzien worden na feedback van Eduardo over welke velden per SKM relevant zijn. Volgende keer eerst een korte afstemming doen voor ik begin met het schema.
- De compatibiliteitsmatrix is op dit moment nog oppervlakkig - voor sommige templates is het onduidelijk of ze "compatible" of "gedeeltelijk compatible" zijn met vintage_977. Moet in Sprint 3 preciezer worden.
- Documentatie (DOCUMENTATION.md) had ik initieel niet gepland maar bleek nodig om het render stack en de custom filters te documenteren. Scope was iets groter dan geschat.

## Action items voor Sprint 1

1. **Eerst afstemmen met Erwin** over variabele-beschikbaarheid per vintage voor de ESIS/loan schedule templates, zodat we niet weer halverwege het schema moeten herzien.
2. **Template migratie in volgorde van complexiteit** - begin met de eenvoudigere templates (ESIS, AV, EID) en bouw op naar de complexere (loan schedules, offer summaries).
3. **Testen met beide taalvarianten** - bij de Generic templates was het makkelijk om NL/FR tegelijk te doen, maar bij complexere templates met conditionele logica moet ik opletten dat de FR-variant niet per ongeluk NL-tekst overneemt (bekend probleem uit het verleden).

## Demo

Sprint 0 demo gegeven aan Eduardo en Erwin op 11 april 2026. Besproken:
- Repository structuur en branching model
- Inventaris resultaten (23 productlijnen, ~1850 bestanden)
- Registry schema en compatibiliteitsmatrix opzet
- Jinja inheritance voorbeeld (Generic empty_letter)
- Planning Sprint 1 (template migratie)
