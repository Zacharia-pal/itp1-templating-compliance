# Sprint 2 Planning

**Sprint:** Sprint 2 - SKM Cleanup + JSM Automations
**Periode:** 28 april - 9 mei 2026
**Capaciteit:** ~52h verdeeld over 8 werkdagen (Vr 1 mei is feestdag, zie onderaan)
**Sprint Goal:** Duplicate SKM templates consolideren in genormaliseerde structuur. Vier JSM automatiseringsworkflows implementeren (git-sync outbound + inbound, daily digest, attachment monitor).

## User Stories

| # | User Story | Pts | Uren | Prio |
|---|-----------|-----|------|------|
| US-13 | Als business analyst wil ik dat duplicate SKM-templates geconsolideerd zijn in een base template per familie met varianten via Jinja inheritance | 8 | 10h | Hoog |
| US-14 | Als ontwikkelaar wil ik een outbound Git-sync workflow die JIRA GIT-tickets automatisch omzet naar GitHub feature branches op de juiste vintage branch | 8 | 10h | Hoog |
| US-15 | Als ontwikkelaar wil ik een inbound Git-sync die PR-merges terugkoppelt naar JIRA (GIT-ticket sluiten, PLVFIN naar Testing Template) | 5 | 7h | Middel |
| US-16 | Als service desk medewerker wil ik een dagelijkse tweetalige (NL/FR) e-mail digest van gewijzigde tickets zodat het team op de hoogte blijft | 8 | 10h | Middel |
| US-17 | Als ontwikkelaar wil ik een attachment monitor die bestanden >400MB naar OneDrive verplaatst met shareable link zodat Backbone/Vortex sync niet breekt | 5 | 7h | Middel |
| - | Sprint planning, standup logs, retrospective, demo | - | 3h | - |
| - | Buffer voor debugging en stakeholder feedback | - | 5h | - |

**Totaal:** ~52h

## Volgorde van werken

1. Eerst SKM consolidatiestrategie afstemmen met Erwin (week 1, dag 1).
2. Pas dan beginnen met dedupliceren - in volgorde Generic varianten, dan HypoSelect/NewHyp shared, daarna verzekeringsproducten.
3. JSM workflows in volgorde: outbound -> inbound -> daily digest -> monitor (per workflow een PR).
4. E-mail templates testen in Outlook desktop, niet enkel in webmail (les uit retro Sprint 1).

## DoD voor deze sprint

- Elke user story heeft een retrospective referentie als hij niet helemaal afkomt.
- Workflows hebben een README die de inputs/outputs beschrijft.
- E-mail digest werkt minimaal 1x in test mailbox voor de demo.
- SKM consolidatie geverifieerd door rendering test op minstens 1 product.

## Risicos

- **Outlook desktop rendering**: bekend probleem. Plan: dual-render fallback met MSO conditional comments.
- **OneDrive sharing policy**: tenant kan anonymous links blokkeren. Plan: fallback naar password-protected of org-wide sharing.
- **Tijdsdruk**: 52h verdeeld over 8 werkdagen is strak. Buffer van 5h ingebouwd voor onvoorziene debugging.

## Sprint Ceremonies

- Sprint planning: dinsdag 28 april, 1u
- Daily standups: 8 entries in wiki (Vr 1 mei overgeslagen)
- Sprint Review/Demo: vrijdag 9 mei, met Eduardo en Erwin
- Sprint Retrospective: vrijdag 9 mei na demo, bespreken met Dirk
- Status emails: 1 per week naar Eduardo (Dirk in cc)

## Belgische feestdagen

- **Vrijdag 1 mei**: Dag van de Arbeid. Geen werk gepland, geen standup, geen entries in projectwerk.
- Werkdagen Sprint 2: Di 28/4, Wo 29/4, Do 30/4, Ma 4/5, Di 5/5, Wo 6/5, Do 7/5, Vr 8/5 (8 dagen).
- Overige feestdagen verderop in het project: Do 14 mei OLH Hemelvaart (Sprint 3), Ma 25 mei Pinkstermaandag (voor buffer).
