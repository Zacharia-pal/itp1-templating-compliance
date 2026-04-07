# Compatibiliteitsmatrix

## Overzicht

Deze matrix toont welke templates compatibel zijn met welke vFinance-vintage. Een ✅ betekent dat de template volledig werkt op die vintage. Een ⚠️ betekent dat er kleine variabele-verschillen zijn die niet breaking zijn. Een ❌ betekent dat de template niet compatible is.

**Status:** Skeleton  - wordt uitgebreid in Sprint 1 (migratie) en Sprint 3 (volledige invulling)

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
| **Generic** | empty_letter | ✅ | ✅ | ✅ | Basis template, breed compatible |
| **GenericLoan** | empty_letter | ⚠️ | ✅ | ✅ | Uitgebreide address meta tags |
| | GBL_HYP_* | ⚠️ | ✅ | ✅ | 15+ varianten |
| **Life_Insurance** | contract | ❌ | ✅ | ✅ | Complexe includes, nieuwe roles structuur |
| | amendment | ❌ | ✅ | ✅ | XMP metadata vereist |
| | account_movements | ⚠️ | ✅ | ✅ | Letter variant toegevoegd in 1074 |
| | transaction | ✅ | ✅ | ✅ | |
| **NewHyp** | esis | ❌ | ✅ | ✅ | Geïndexeerde aflossingsplan (loan_schedule_index) |
| | agreement | ⚠️ | ✅ | ✅ | |
| **Wet4892** | esis | ❌ | ✅ | ✅ | Complexe loan schedule decision logic |
| | offer_summary | ❌ | ✅ | ✅ | Beslissingsboom voor asset values |
| | decision | ⚠️ | ✅ | ✅ | |
| **Roerend** | agreement | ✅ | ✅ | ✅ | |
| | secci | ✅ | ✅ | ✅ | |
| **HypoSelect** | contract | ⚠️ | ✅ | ✅ | |
| | proposal | ⚠️ | ✅ | ✅ | |
| **Short_Term_Cover** | contract | ✅ | ✅ | ✅ | |

---

## Shared Includes

| Include | vintage_977 | vintage_1074 | vintage_1210 | Opmerkingen |
|---------|-------------|--------------|--------------|-------------|
| html_head_nl_BE / fr_BE | ⚠️ | ✅ | ✅ | vintage_977: beperkte NOTIFICATION_HEADER support |
| recipient-header.html | ❌ | ✅ | ✅ | custom_address niet beschikbaar in 977 |
| custom_macros.html | ✅ | ✅ | ✅ | |
| loan_schedule | ❌ | ✅ | ✅ | Index detection vereist 1074+ |
| signatures.html | ✅ | ✅ | ✅ | |

---

## Samenvatting

| Vintage | Volledig compatible | Gedeeltelijk | Niet compatible |
|---------|-------------------|--------------|-----------------|
| vintage_977 | ~40% | ~30% | ~30% |
| vintage_1074 | 100% | 0% | 0% |
| vintage_1210 | 100% | 0% | 0% |

> **Conclusie:** vintage_1074 is de referentiebranch. Alle templates zijn primair ontwikkeld en getest voor deze vintage. Oudere vintages hebben beperkte compatibiliteit, vooral voor complexe templates met nieuwe variabelen (loan schedules, custom addresses, XMP metadata).
