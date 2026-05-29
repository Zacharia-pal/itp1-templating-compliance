# Sprint 2 Retrospective

**Sprint:** Sprint 2 - SKM Cleanup + JSM Automations
**Periode:** 28 april - 8 mei 2026
**Uren gelogd:** ~52h

## Sprint Goal

Duplicate SKM-templates consolideren via Jinja inheritance, en vier JSM automatiseringsworkflows opzetten (outbound git-sync, inbound git-sync, daily digest, attachment monitor).

## Wat ging goed

- De afstemming met Erwin meteen op dag 1 was goud waard. Mijn aanname dat Boutique_44 ook REGData/SIData had klopte niet, die fiches zitten enkel bij Boutique_23, Evolis en Patronale_Life_Flexible. Was ik meteen beginnen dedupliceren zoals oorspronkelijk gepland, dan had ik een hoop werk voor niets gedaan. De action item uit Sprint 1 (eerst de varianten in kaart brengen met Erwin) heeft dus echt gewerkt.
- De Generic21/23/44 consolidatie viel mee. Generic23 als familie-base nemen en de andere twee laten erven was een kleine ingreep met veel effect. Tak 21 had enkel de invoice_state regel extra, die zit nu netjes in een aparte include.
- De JSM workflows incrementeel bouwen (action item 2 uit Sprint 1) hielp echt. Per workflow een aparte commit en test, niet alles in een keer. Outbound, inbound en digest zaten zo binnen drie dagen werkend.
- De Outlook desktop fallback (inline styles + MSO comments) die ik in de Sprint 1 retro al had voorzien werkte meteen. De digest rendert nu correct in webmail en in Outlook desktop.

## Wat kan beter

- De attachment monitor (US-17) is niet helemaal af. De basis werkt voor bestanden net boven 400MB, maar Microsoft Graph vereist een upload session voor alles boven 250MB. Die heb ik nog niet netjes geimplementeerd, dus de workflow staat nog niet live. Staat als TODO in het script. Schuift door naar Sprint 3.
- Ik heb maar een handvol ng-codes gemigreerd, niet alle ~60 paren. Het patroon staat vast en is bewezen, maar het echte volume is mechanisch werk dat ik bewust naar Sprint 3 heb geschoven. Risico is dat ik dat onderschat qua tijd.
- De transition-ids voor de JIRA workflow zitten nog hardcoded in de scripts (In Progress, Done, Testing Template). Werkt nu, maar als het workflow scheme verandert breekt het stil. Beter uit een config halen, ook op de TODO-lijst.

## Action items voor Sprint 3

1. **Attachment monitor afmaken** - Graph upload session voor bestanden > 250MB, dan pas de workflow live zetten.
2. **Resterende ng-codes migreren** - de volledige REGData/SIData set voor Boutique_23, Evolis en Patronale_Life_Flexible, volgens het bewezen patroon.
3. **Transition-ids en config externaliseren** - de hardcoded waarden in de JSM scripts naar de config file halen.
4. **CI pipeline opzetten** - template-validatie (render test) zodat een kapotte extends meteen opvalt. Dit was sowieso al Sprint 3 scope.

## Demo

Sprint 2 demo gegeven aan Eduardo en Erwin op 8 mei 2026. Besproken:

- SKM consolidatie: Generic21/23/44 via een gedeelde base, en de gedeelde REGData/SIData base voor de boutique-producten
- Short_Term_Cover movements naar de Life_Insurance base
- De drie werkende JSM workflows (outbound, inbound, digest) live gedemonstreerd op een testticket
- De digest mail in NL en FR, ook getoond in Outlook desktop
- Stand van zaken attachment monitor en waarom die nog niet live staat
