# Sprint 3 Planning

**Sprint:** Sprint 3 - CI, ng-fiches, docs en release
**Periode:** 11 mei - 22 mei 2026
**Capaciteit:** ~48h over 8 werkdagen (Do 14 mei Hemelvaart en de brugdag Vr 15 mei eruit)
**Sprint Goal:** De automatisering afronden met een CI die templates valideert, de resterende ng-fiches genereren, alles documenteren voor overdracht en de vintage_1074 set naar release brengen.

## User Stories

| # | User Story | Pts | Uren | Prio |
|---|-----------|-----|------|------|
| US-18 | Als ontwikkelaar wil ik een CI die op elke push checkt of alle templates parsen en of de extends/include verwijzingen kloppen | 5 | 7h | Hoog |
| US-19 | Als beheerder wil ik de JSM transition-ids en ontvangers in een config ipv hardcoded zodat een scheme-wijziging niet stil breekt | 3 | 4h | Middel |
| US-13 | Als business analyst wil ik de resterende REGData/SIData ng-fiches gemigreerd, bij voorkeur gegenereerd uit een fondsenlijst | 8 | 10h | Hoog |
| US-17 | Als ontwikkelaar wil ik de attachment monitor afwerken met een upload session voor bestanden > 250MB | 5 | 7h | Middel |
| US-20 | Als opvolger wil ik een handover-document zodat ik het systeem kan overnemen | 5 | 6h | Hoog |
| - | Stakeholder validatie + fixes | - | 5h | - |
| - | Release prep (registry 1.0.0) + ceremonies | - | 6h | - |

**Totaal:** ~48h

## Volgorde van werken

1. CI eerst, zodat de rest van de sprint meteen gevalideerd wordt bij elke push.
2. Config externaliseren (snelle action item uit de Sprint 2 retro).
3. ng-fiches genereren via een script ipv handwerk.
4. Attachment monitor afwerken.
5. Documentatie en release op het einde.

## DoD voor deze sprint

- CI staat groen op de werkbranch.
- Alle templates valideren (parse + verwijzingen).
- Handover document is leesbaar voor iemand buiten het project.
- Registry op 1.0.0, compat matrix bijgewerkt.

## Belgische feestdagen

- **Donderdag 14 mei**: OLH Hemelvaart. Geen werk, geen standup.
- **Vrijdag 15 mei**: brugdag, ook vrij genomen.
- Werkdagen Sprint 3: Ma 11, Di 12, Wo 13, Ma 18, Di 19, Wo 20, Do 21, Vr 22 (8 dagen).

## Sprint Ceremonies

- Sprint planning: maandag 11 mei
- Daily standups: 8 entries
- Sprint Review/Demo: vrijdag 22 mei, met Eduardo en Erwin
- Sprint Retrospective: vrijdag 22 mei na de demo
