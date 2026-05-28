**Aan:** eduardo.de.almeida.raposo@patronale-life.be
**Cc:** dirk.hostens@vives.be, erwin.geeraerts@patronale-life.be
**Onderwerp:** ITP1 Sprint 2 status en demo

Dag Eduardo,

Een korte tussenstand voor Sprint 2 (28 april - 8 mei), de sprint rond SKM consolidatie en de JSM automatisering.

**Status**

SKM consolidatie:

- Generic21, Generic23 en Generic44 erven nu van een gedeelde base ipv bijna-identieke kopieen. Generic23 is de familie-base, Generic21 voegt enkel de Tak 21 invoice override toe.
- Gedeelde REGData/SIData base voor de ng-fiches. Na overleg met Erwin gaat het om Boutique_23, Evolis en Patronale_Life_Flexible (Boutique_44 heeft die fiches niet). Eerste codes gemigreerd, de rest volgt hetzelfde patroon in Sprint 3.
- Short_Term_Cover account_movements trekt nu ook op de Life_Insurance base.

JSM automatisering:

- Outbound git-sync: open GIT-tickets worden automatisch feature branches op de juiste vintage.
- Inbound git-sync: een gemergede PR sluit het GIT-ticket en zet de gelinkte template-ticket op Testing Template.
- Dagelijkse digest: tweetalige NL/FR mail van gewijzigde tickets, rendert correct in Outlook desktop.
- Attachment monitor (>400MB naar OneDrive): basis staat, maar de Graph upload session voor grote bestanden is nog niet af. Die zet ik pas live in Sprint 3.

Registry is bijgewerkt naar 0.3.0 en de compatibiliteitsmatrix is uitgebreid met de Sprint 2 templates.

**Demo**

Demo gegeven op vrijdag 8 mei, met focus op de consolidatie via overerving en de drie werkende JSM workflows op een testticket.

**Volgende sprint**

Sprint 3 (11 mei - 22 mei) gaat over de CI pipeline voor template-validatie, de resterende ng-codes, de attachment monitor afwerken, en de documentatie en stakeholdervalidatie richting release.

Als er opmerkingen zijn over Sprint 2 hoor ik het graag.

Met vriendelijke groeten
Zacharia
