**Aan:** eduardo.de.almeida.raposo@patronale-life.be
**Cc:** dirk.hostens@vives.be, erwin.geeraerts@patronale-life.be
**Onderwerp:** ITP1 Sprint 3 status en demo

Dag Eduardo,

De laatste reguliere sprint (Sprint 3, 11 - 22 mei) zit erop. Hieronder de stand van zaken.

**Status**

- CI-validatie: elke push en PR checkt nu of alle templates parsen en of de extends/include paden bestaan. Staat groen. Heeft tijdens de sprint al twee fouten in de ng-generator gevangen.
- ng-fiches: ipv handwerk gegenereerd uit een fondsenlijst (config/ng_funds.json). 115 REGData/SIData fiches voor Boutique_23, Evolis en Patronale_Life_Flexible. Een nieuw fonds toevoegen is nu een regel config.
- JSM config: de transition-ids en digest-ontvangers staan niet meer hardcoded maar in de config.
- Handover documentatie: docs/handover.md, klaar voor het team.
- Registry naar 1.0.0, compatibiliteitsmatrix op release voor de vintage_1074 set.

**Open punt**

De attachment monitor is functioneel af, inclusief de upload session voor grote bestanden, maar staat bewust nog niet live. Hij verwijdert bijlagen in productie-JIRA, dus dat wil ik pas aanzetten na jullie go en op een apart service-account in plaats van mijn persoonlijk token. Graag even afstemmen met Erwin wanneer dat past.

**Demo**

Demo gegeven op vrijdag 22 mei: de CI live, de ng-generator, de config-externalisatie en de handover.

**Bufferweek (26 - 29 mei)**

Ik gebruik de bufferweek voor het groeiportfolio en de slotpresentatie, en voor de afstemming over de attachment monitor.

Bedankt voor de begeleiding deze sprints. Met vriendelijke groeten,
Zacharia
