# Sprint 1 Retrospective

**Sprint:** Sprint 1 - Template Migration
**Periode:** 14 april - 25 april 2026
**Uren gelogd:** ~52h

## Sprint Goal

Migratie van prioritaire templates (ESIS, AV, EID, loan schedules, offer summary, agreement) van visuele XML naar Jinja HTML met inheritance. XMP metadata opzetten. Registry en compatibiliteitsmatrix bijwerken.

## Wat ging goed

- De volgorde "eenvoudig naar complex" hielp echt: door eerst de Jinja base templates te bouwen en daarna ESIS te doen, kon ik de inheritance pattern eerst valideren met een eenvoudige template voordat ik ermee aan de slag ging op de complexere documenten zoals offer_summary.
- HypoSelect en Wet4892 ESIS konden bijna volledig hergebruikt worden via {% extends %} van de NewHyp ESIS. Dat bevestigt dat de blockstructuur goed gekozen is.
- De refactor op het einde (Generic en GenericLoan empty_letter terug laten extenden van _shared/_base_letter) was klein van scope maar maakt de codebase een stuk consistenter.

## Wat kan beter

- De index detection in loan_schedule liet me zien hoe fragiel string-vergelijkingen zijn zodra je met gelokaliseerde data werkt. De fix was simpel (op de ruwe waarde vergelijken) maar het had me wel een halve dag gekost om de root cause te vinden. Volgende keer eerst checken of er een numerieke variant beschikbaar is voor dergelijke checks.
- De offer_summary FR-bug (block inheritance naar de verkeerde base) was eigenlijk een copy-paste fout. Even dom, maar wel gevangen door de demo voor te bereiden in beide talen. Volgende keer altijd FR rendering nakijken na een copy van de NL variant.
- De verdeling over de twee weken was scheef: ik heb het zware migratiewerk in week 1 op enkele lange dagen gedaan (Wo en Do liepen flink uit), waardoor week 2 vrij rustig was. Volgende sprint wil ik het werk gelijkmatiger over de werkdagen verdelen zodat ik niet 14h-dagen klop.

## Action items voor Sprint 2

1. **Kies de SKM consolidatiestrategie eerst expliciet met Erwin** - voor sommige templates lijkt deduplicatie op het oog mogelijk maar er zitten subtiele varianten in tussen Generic21/23/44. Niet beginnen voor we die varianten in kaart hebben.
2. **JSM workflows incrementeel bouwen, niet in een big bang** - eerst git-sync outbound werkend krijgen, dan inbound, dan daily digest, dan attachment monitor. Per workflow een PR.
3. **E-mail templates testen in Outlook desktop, niet alleen webmail** - bekend probleem dat dingen breken in Outlook desktop. Dual rendering voorzien zodra nodig.

## Demo

Sprint 1 demo gegeven aan Eduardo en Erwin op 25 april 2026. Besproken:

- Jinja inheritance pattern (NewHyp ESIS -> HypoSelect / Wet4892 met blocks)
- Loan schedule index detection inclusief de gevonden bug en fix
- Offer summary beslissingsboom KBI vs schatting
- Account movements + transaction voor Life_Insurance en Boutique_23 reuse
- Updated registry (0.2.0) en compatibiliteitsmatrix
- Refactor naar gedeelde _shared/_base_letter en _base_document
