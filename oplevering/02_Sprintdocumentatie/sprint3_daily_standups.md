# Sprint 3 - Daily Standups

## Maandag 11 mei

**Wat heb ik gedaan?**
Sprint 2 afgesloten vrijdag. Sprint 3 backlog gerefined en planning gedocumenteerd.

**Wat ga ik vandaag doen?**
Sprint planning, en daarna de CI opzetten: een GitHub Action die op elke push checkt of alle templates parsen en of de extends/include paden bestaan. Zo vangen we een kapot pad meteen.

**Blokkades?**
Geen.

---

## Dinsdag 12 mei

**Wat heb ik gedaan?**
CI staat. Een validator die alle 87 templates parset en de verwijzingen checkt, draait op push en PR. Alles groen.

**Wat ga ik vandaag doen?**
Snelle action item uit de Sprint 2 retro afwerken: de transition-ids en de digest-ontvangers uit de scripts halen en in de config zetten. Die stonden nog hardcoded.

**Blokkades?**
Geen.

---

## Woensdag 13 mei

**Wat heb ik gedaan?**
Config externalisatie af. Outbound, inbound en digest lezen nu uit jsm_sync.example.json.

**Wat ga ik vandaag doen?**
De resterende ng-fiches. Ik ga ze niet met de hand maken maar een generator schrijven die ze uit een fondsenlijst genereert. Dat is sneller en consistenter.

**Blokkades?**
Geen, maar ik verwacht wat trial en error met de Jinja escaping in de generator.

---

## Maandag 18 mei

**Wat heb ik gedaan?**
Donderdag Hemelvaart en vrijdag brugdag vrij genomen. De generator van woensdag werkte na twee foutjes die de CI netjes opving (een verkeerd base-pad en een %%-escape in de generator). 115 fiches gegenereerd, alles valideert.

**Wat ga ik vandaag doen?**
De attachment monitor afwerken: de upload session voor bestanden boven 250MB, want een gewone PUT lukt maar tot die grens.

**Blokkades?**
De monitor verwijdert bijlagen in productie-JIRA. Ik laat de code af maar zet de workflow nog niet live tot Erwin akkoord is en we een apart service-account hebben ipv mijn persoonlijk token. Voorlopig dus niet gepusht.

---

## Dinsdag 19 mei

**Wat heb ik gedaan?**
Upload session code af en lokaal getest met chunks. Workflow staat klaar maar bewust nog niet live.

**Wat ga ik vandaag doen?**
Handover documentatie schrijven: mappenstructuur, hoe een template of ng-fiche toevoegen, de workflows, secrets en de open punten.

**Blokkades?**
Geen.

---

## Woensdag 20 mei

**Wat heb ik gedaan?**
Handover doc af.

**Wat ga ik vandaag doen?**
Validatiesessie met Erwin. Hij kijkt de fiches na, ik verwerk de feedback. Eerste punt al binnen: label "Beheerder" mag duidelijker.

**Blokkades?**
Geen.

---

## Donderdag 21 mei

**Wat heb ik gedaan?**
Feedback Erwin verwerkt: "Fondsbeheerder" ipv "Beheerder" en een compartiment-regel toegevoegd in de gedeelde base, dus alle fiches erven het.

**Wat ga ik vandaag doen?**
Release prep. Registry naar 1.0.0, de vintage_1074 set is gevalideerd via de CI en gaat naar release. Compat matrix bijwerken.

**Blokkades?**
Geen.

---

## Vrijdag 22 mei

**Wat heb ik gedaan?**
Registry op 1.0.0, matrix op release.

**Wat ga ik vandaag doen?**
Sprint 3 demo aan Eduardo en Erwin. Retrospective schrijven, status mail opmaken. Bespreken wat er in de bufferweek nog moet (groeiportfolio finaal, slotpresentatie).

**Blokkades?**
Geen.
