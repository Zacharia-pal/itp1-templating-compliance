# Compatibiliteitsmatrix

## Overzicht

Deze matrix toont welke templates compatibel zijn met welke vFinance-vintage. Een ✅ betekent dat de template volledig werkt op die vintage. Een ⚠️ betekent dat er kleine variabele-verschillen zijn die niet breaking zijn. Een ❌ betekent dat de template niet compatible is.

**Status:** Sprint 1 afgerond - ESIS, AV, EID, loan_schedule, offer_summary, agreement, account_movements en transaction toegevoegd. Sprint 3 dekt de overige templates en finaliseert.

---

## Document Templates

| Product | Template | vintage_977 | vintage_1074 | vintage_1210 | Opmerkingen |
|---------|----------|-------------|--------------|--------------|-------------|
| **Boutique_23** | contract | ⚠️ | ✅ | ✅ | vintage_977: recipient.custom_address niet beschikbaar |
| | certificate | ✅ | ✅ | ✅ | |
| | eid | ✅ | ✅ | ✅ | |
| | account_movements | ✅ | ✅ | ✅ | |
| | REGData/SIData (ng_*) | ✅ | ✅ | ✅ | ~60 paren per type |
| **Credit_Insurance** | contract | ❌ | ✅ | ✅ | vintage_977: ontbrekende velden |
| | medical_questionnaire | ✅ | ✅ | ✅ | 3 varianten: A2, QMNP, QMOB |
| | av | ❌ | ✅ | ✅ | Override verplichtingen voor schuldsaldoverzekering |
| **Generic** | empty_letter | ✅ | ✅ | ✅ | Basis template, breed compatible |
| | av | ❌ | ✅ | ✅ | 8 secties via blocks, productspecifieke overrides |
| | eid | ⚠️ | ✅ | ✅ | Loop over persons, vintage_977 mist national_number formatting |
| | agreement | ⚠️ | ✅ | ✅ | Generic basis voor alle agreement varianten |
| | certificate | ⚠️ | ✅ | ✅ | Coverpage + packages-blok |
| **GenericLoan** | empty_letter | ⚠️ | ✅ | ✅ | Uitgebreide address meta tags |
| | GBL_HYP_* | ⚠️ | ✅ | ✅ | 15+ varianten |
| **Life_Insurance** | contract | ❌ | ✅ | ✅ | Complexe includes, nieuwe roles structuur |
| | amendment | ❌ | ✅ | ✅ | XMP metadata vereist |
| | account_movements | ⚠️ | ✅ | ✅ | Letter variant toegevoegd in 1074, XMP gekoppeld |
| | transaction | ✅ | ✅ | ✅ | Bevestigingsbrief enkelvoudige transactie |
| | av | ❌ | ✅ | ✅ | Override definities + verplichtingen via super() |
| **NewHyp** | esis | ❌ | ✅ | ✅ | Geïndexeerde aflossingsplan (loan_schedule_index) |
| | agreement | ⚠️ | ✅ | ✅ | |
| | loan_schedule | ❌ | ✅ | ✅ | Index detection vereist 1074, gefixed in 1.1.0 |
| **Wet4892** | esis | ❌ | ✅ | ✅ | Complexe loan schedule decision logic, super() voor extra warnings |
| | offer_summary | ❌ | ✅ | ✅ | Beslissingsboom KBI vs schatting, XMP metadata |
| | decision | ⚠️ | ✅ | ✅ | |
| **Roerend** | agreement | ✅ | ✅ | ✅ | |
| | secci | ✅ | ✅ | ✅ | |
| **HypoSelect** | contract | ⚠️ | ✅ | ✅ | |
| | proposal | ⚠️ | ✅ | ✅ | |
| | esis | ❌ | ✅ | ✅ | Extends NewHyp ESIS, alleen subtitle override |
| **Short_Term_Cover** | contract | ✅ | ✅ | ✅ | |

---

## Shared Includes

| Include | vintage_977 | vintage_1074 | vintage_1210 | Opmerkingen |
|---------|-------------|--------------|--------------|-------------|
| html_head_nl_BE / fr_BE | ⚠️ | ✅ | ✅ | vintage_977: beperkte NOTIFICATION_HEADER support, XMP-include nieuw in 1074 |
| recipient-header.html | ❌ | ✅ | ✅ | custom_address niet beschikbaar in 977 |
| custom_macros.html | ✅ | ✅ | ✅ | |
| macros/html.html | ❌ | ✅ | ✅ | Sprint 1 toevoeging (render_table, render_td, currency, percentage, hypo_header) |
| _shared/_base_letter.html | ❌ | ✅ | ✅ | Sprint 1: gedeelde brief-base met letter_main block |
| _shared/_base_document.html | ❌ | ✅ | ✅ | Sprint 1: document-base voor contracten/ESIS |
| _shared/macros_currency.html | ❌ | ✅ | ✅ | BE-formatting voor bedrag/datum |
| _shared/roles.html | ❌ | ✅ | ✅ | Personen-overzicht voor polis/contract |
| loan_schedule | ❌ | ✅ | ✅ | Index detection vereist 1074+, gefixed in 1.1.0 |
| signatures.html | ✅ | ✅ | ✅ | |
| xmp/xmp_base.xml | ❌ | ✅ | ✅ | XMP metadata basis voor PDF-archivering |

---

## Samenvatting

| Vintage | Volledig compatible | Gedeeltelijk | Niet compatible |
|---------|-------------------|--------------|-----------------|
| vintage_977 | ~30% | ~25% | ~45% |
| vintage_1074 | 100% | 0% | 0% |
| vintage_1210 | 100% | 0% | 0% |

> Cijfer voor vintage_977 daalde licht omdat de Sprint 1 templates (XMP, _shared/_base, macros/html) niet beschikbaar zijn op die oude vintage. Dat is verwacht: vintage_977 is bevroren voor klanten die nog niet upgrade-baar waren.

> **Conclusie:** vintage_1074 is de referentiebranch. Alle templates zijn primair ontwikkeld en getest voor deze vintage. Oudere vintages hebben beperkte compatibiliteit, vooral voor complexe templates met nieuwe variabelen (loan schedules, custom addresses, XMP metadata).
