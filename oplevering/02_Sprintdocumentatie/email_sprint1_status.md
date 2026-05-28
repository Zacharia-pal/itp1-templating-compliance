**Aan:** eduardo.de.almeida.raposo@patronale-life.be
**Cc:** dirk.hostens@vives.be, erwin.geeraerts@patronale-life.be
**Onderwerp:** ITP1 Sprint 1 status en demo planning

Dag Eduardo,

Hieronder een korte tussenstand voor Sprint 1 (14-25 april), het zwaartepunt van de template migratie.

**Status**

Alle gemigreerde Sprint 1 templates staan op de vintage_1074 branch:

- ESIS voor NewHyp, HypoSelect en Wet4892 (NL+FR)
- AV (Generic, Life_Insurance, Credit_Insurance) met productspecifieke overrides
- EID identiteitstemplates (Generic, Boutique_23)
- Loan schedule (NewHyp basis, HypoSelect/Wet4892 overerving) inclusief fix voor index detection bij gelokaliseerde bedragen
- Offer summary Wet4892 met beslissingsboom KBI vs schatting
- Agreement templates (NewHyp, Roerend)
- Account movements + transaction voor Life_Insurance en Boutique_23
- XMP metadata XML-includes ingehaakt in html_head

Registry is bijgewerkt naar versie 0.2.0 met de nieuwe entries en compatibiliteitsmatrix is uitgebreid.

**Demo**

Ik wil graag op vrijdag 25 april kort de demo geven, ~30 min, met focus op:

- Jinja inheritance via NewHyp ESIS -> HypoSelect/Wet4892
- Loan schedule index detection en de gevonden bug/fix
- Offer summary beslissingsboom

**Volgende sprint**

Sprint 2 (28 april - 9 mei) gaat over SKM consolidatie en de JSM automatisering (git-sync outbound + inbound, daily digest, attachment monitor). Ik plan een korte afstemming met Erwin om eerst de SKM varianten goed in kaart te hebben voor we beginnen met dedupliceren.

Als er vooraf nog opmerkingen zijn over Sprint 1, hoor ik graag.

Met vriendelijke groeten
Zacharia
