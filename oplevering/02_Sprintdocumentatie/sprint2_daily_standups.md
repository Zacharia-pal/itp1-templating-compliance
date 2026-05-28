# Sprint 2 - Daily Standups

## Dinsdag 28 april

**Wat heb ik gedaan?**
Sprint 1 demo gegeven, retrospective geschreven, status email naar Eduardo gestuurd. Sprint 2 backlog gerefined en planning gedocumenteerd.

**Wat ga ik vandaag doen?**
Eerst afstemming met Erwin over de SKM varianten (Generic21 vs Generic23 vs Generic44, en HypoSelect/NewHyp shared structuur). Daarna een eerste analyse-document opstellen met welke templates kandidaat zijn voor consolidatie.

**Blokkades?**
Geen. Erwin is beschikbaar deze namiddag.

---

## Woensdag 29 april

**Wat heb ik gedaan?**
Gisteren met Erwin de SKM varianten doorgenomen. Belangrijkste les: Boutique_44 heeft helemaal geen REGData/SIData, dat dacht ik fout. De ng-fiches zitten enkel bij Boutique_23, Evolis en Patronale_Life_Flexible. Analyse-document bijgewerkt.

**Wat ga ik vandaag doen?**
Beginnen met de Generic consolidatie. Generic21, Generic23 en Generic44 zijn bijna identiek. Plan: Generic23 als familie-base, Generic44 erft daarvan, Generic21 krijgt enkel de Tak 21 invoice override erbij.

**Blokkades?**
Geen.

---

## Donderdag 30 april

**Wat heb ik gedaan?**
Generic21/23/44 geconsolideerd via overerving en gecommit. Eerste rendering test op Generic23 movements zag er goed uit.

**Wat ga ik vandaag doen?**
De gedeelde REGData/SIData base opzetten in _shared_boutique en de eerste ng-codes migreren als voorbeeld. Daarnaast Short_Term_Cover account_movements naar de Life_Insurance base trekken.

**Blokkades?**
Geen, maar de ng-codes zijn er veel (~60 per type). Ik migreer er nu een paar als bewijs van het patroon, de rest doe ik in Sprint 3 want het is mechanisch werk.

---

## Maandag 4 mei

**Wat heb ik gedaan?**
Vrijdag 1 mei niet gewerkt (feestdag). Weekend ook niet. SKM consolidatie deel staat dus klaar.

**Wat ga ik vandaag doen?**
Starten met de JSM automatisering. Eerst de outbound git-sync: open GIT-tickets in PLVFIN omzetten naar feature branches op de juiste vintage. Per ticket een branch, ticket op In Progress.

**Blokkades?**
Even uitzoeken welke transition-id In Progress is in het PLVFIN workflow scheme. Voorlopig gehardcode, moet ik later netter maken.

---

## Dinsdag 5 mei

**Wat heb ik gedaan?**
Outbound sync werkt in een test, branch wordt netjes aangemaakt vanaf de vintage en het ticket gaat naar In Progress.

**Wat ga ik vandaag doen?**
Inbound git-sync: als een PR gemerged is de GIT-ticketkey uit de branchnaam halen, ticket op Done zetten en de gelinkte PLVFIN template-ticket op Testing Template.

**Blokkades?**
Geen.

---

## Woensdag 6 mei

**Wat heb ik gedaan?**
Inbound sync af. Branchnaam parsing werkt, gelinkte ticket wordt mee verzet.

**Wat ga ik vandaag doen?**
De dagelijkse digest mail bouwen, tweetalig NL/FR. Tickets die in de laatste 24u gewijzigd zijn in een overzicht naar Eduardo en Erwin.

**Blokkades?**
Outlook desktop rendering zoals verwacht lastig. Ik los het op met inline styles en MSO conditional comments, dat is de fallback die ik in de retro van Sprint 1 al had voorzien.

---

## Donderdag 7 mei

**Wat heb ik gedaan?**
Digest verstuurd naar een test-mailbox, rendert correct in zowel webmail als Outlook desktop.

**Wat ga ik vandaag doen?**
De attachment monitor: bijlagen boven 400MB naar OneDrive verplaatsen via Graph en de bijlage in JIRA vervangen door een share-link. Dit is de laatste van de vier workflows.

**Blokkades?**
Graph laat maar 250MB toe via een gewone PUT, daarboven moet je een upload session gebruiken. Dat krijg ik vandaag waarschijnlijk niet meer netjes af, ik zet het als TODO en test voorlopig met bestanden net boven 400MB op een andere manier.

---

## Vrijdag 8 mei

**Wat heb ik gedaan?**
Attachment monitor staat lokaal maar de upload session is nog niet af, dus die workflow zet ik nog niet live.

**Wat ga ik vandaag doen?**
Registry naar 0.3.0 en de compatibiliteitsmatrix bijwerken voor de Sprint 2 templates. Demo aan Eduardo en Erwin, retrospective schrijven en de status mail opmaken.

**Blokkades?**
Geen.
