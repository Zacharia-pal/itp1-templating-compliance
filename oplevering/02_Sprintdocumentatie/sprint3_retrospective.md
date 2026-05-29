# Sprint 3 Retrospective

**Sprint:** Sprint 3 - CI, ng-fiches, docs en release
**Periode:** 11 mei - 22 mei 2026
**Uren gelogd:** ~48h

## Sprint Goal

De automatisering afronden met een CI-validatie, de resterende ng-fiches genereren, alles documenteren voor overdracht en de vintage_1074 set naar release brengen.

## Wat ging goed

- De CI als eerste opzetten was de juiste keuze. Ze heeft zich diezelfde sprint al bewezen: tijdens het bouwen van de ng-generator ving ze twee fouten (een verkeerd base-pad en een %%-escape die niet collapste). Zonder CI had ik die pas gezien bij het genereren in productie. Precies het soort bug dat in Sprint 1 nog een halve dag kostte.
- De ng-fiches genereren ipv handmatig maken was veel sneller. Een fondsenlijst in JSON en een generator van een 80 regels maakte 115 bestanden. En het is herbruikbaar: een nieuw fonds toevoegen is nu een regel in de config.
- De handover schrijven dwong me om de losse eindjes expliciet te benoemen. Daardoor staat nu zwart op wit wat af is en wat niet.

## Wat kan beter

- De attachment monitor staat nog steeds niet live. De code is wel af (incl. upload session), maar omdat hij bijlagen in productie verwijdert wil ik dat niet aanzetten zonder go van Erwin en zonder een apart service-account. Dat is de juiste voorzichtigheid, maar het betekent wel dat US-17 over twee sprints is blijven hangen. Les: een story die productie-data wijzigt vroeger als "behoeft sign-off" markeren in de planning.
- De FR SIData fiches vallen nog terug op de NL base. Werkt, maar netjes is anders. Staat als TODO in de generator en de handover.
- Ik heb de bufferweek nu echt nodig voor het groeiportfolio en de slotpresentatie. Was misschien beter om daar in elke sprint al een half uurtje aan te besteden ipv het op te sparen.

## Action items voor de bufferweek

1. **Groeiportfolio v3 finaliseren** met de Sprint 2 en 3 reflectie.
2. **Slotpresentatie voorbereiden** (demo van de hele flow: ticket -> branch -> PR -> testing).
3. **Attachment monitor**: met Erwin afstemmen over service-account en go/no-go voor productie.
4. **FR SIData base** opzetten als er tijd over is.

## Demo

Sprint 3 demo gegeven aan Eduardo en Erwin op 22 mei 2026. Besproken:

- De CI-validatie live, inclusief een bewust kapotte template om te tonen dat ze faalt
- De ng-generator en hoe een nieuw fonds toevoegen werkt
- De config-externalisatie van de JSM workflows
- De handover documentatie
- Registry 1.0.0 en de release-status, en de open punten (attachment monitor, FR sidata)
