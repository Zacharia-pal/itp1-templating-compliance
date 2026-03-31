# Template Inventaris

## Overzicht

Dit document biedt een volledig overzicht van alle bestaande templates in het vFinance Sideloader-systeem. De inventaris is opgesteld als basis voor de migratie van visuele XML naar Jinja HTML en de consolidatie van duplicaten.

**Datum inventaris:** 31 maart 2026
**Bron:** PatronaleLife/vFinance_Sideloader repository (vintage_1074 branch)
**Totaal aantal bestanden:** ~1.850 (inclusief NL/FR varianten, REGData/SIData)

---

## Productlijnen

| # | Productlijn | Type | Templates | NL/FR | REGData | SIData | Includes | XMP | Status |
|---|------------|------|-----------|-------|---------|--------|----------|-----|--------|
| 1 | Boutique_23 | Leven (Tak 23) | contract, certificate, eid, account_movements, account_state, ng, sid | Ja | ~60 paren | ~60 paren | Nee | Nee | Actief |
| 2 | Boutique_44 | Leven (Tak 44) | account_movements, account_state, certificate | Ja | Nee | Nee | Nee | Nee | Actief |
| 3 | Credit_Insurance | Kredietverzekering | contract, proposal, pledge, medical_questionnaire (A2/QMNP/QMOB), medical_report, sepa_mandate, transfer_of_benefit | Ja | Nee | Nee | Nee | account_creation.xml | Actief |
| 4 | Evolis | Leven | contract, eid, ng, sid | Ja | ~18 paren | ~18 paren | Nee | Nee | Actief |
| 5 | Fix_21 | Vast rendement (Tak 21) | account_movements, account_state, certificate, contract, eid | Ja | Nee | Nee | Nee | Nee | Actief |
| 6 | Fork_Account | Vork rekening | EID, account_movements, account_state, certificate, contract | Ja | Nee | Nee | Nee | Nee | Actief |
| 7 | Fork_Corporate_Plus | Vork bedrijf | EID, account_movements, account_state, certificate, contract | Ja | Nee | Nee | Nee | Nee | Actief |
| 8 | FructiStarSafe21 | Tak 21 | account_movements, account_state, certificate, contract, eid | Ja | Nee | Nee | Nee | Nee | Actief |
| 9 | Generic | Generiek | empty_letter, GBL_ALG_SEP | Ja | Nee | Nee | Nee | Nee | Actief |
| 10 | Generic21 | Generiek Tak 21 | GBL_VER_* (5 types), account_movements, account_state, certificate | Ja | Nee | Nee | invoice_state_override | Nee | Actief |
| 11 | Generic23 | Generiek Tak 23 | account_movements, account_state, certificate | Ja | Nee | Nee | Nee | Nee | Actief |
| 12 | Generic44 | Generiek Tak 44 | account_movements, account_state, certificate | Ja | Nee | Nee | Nee | Nee | Actief |
| 13 | GenericLoan | Generiek Krediet | GBL_HYP_* (15+ types), GLB_* (10+ types), SKM_HYP_*, approval_extension, correspondence, empty_letter, fireinsurance_*, role_*, sepa_refuse, signatures, transfer_of_income | Ja | Nee | Nee | 20+ includes (advance_composition, aggregate_borrowers, appearance_formula, etc.) | Nee | Actief  - meest complex |
| 14 | HypoSelect | Hypothecair | account_characteristics, bank_transfer, checklist, contract, financial_info, first-notice, general_conditions, proposal | Ja | Nee | Nee | 15+ includes (account_roles, agreed_items, coverage_details, etc.) | Nee | Actief |
| 15 | Investeringskrediet | Investeringskrediet | advance, agreement, first-notice, general_conditions, invoice, loan-completion, loan_application, notice-of-default, repayment_table, sid, signing-agent-settlement, verification_credit_application | Ja | Nee | Nee | 20+ includes (annual_percentage_rate, asset_*, bank_transfer, credit_insurance_*, etc.) | Nee | Actief |
| 16 | Life_Insurance | Levensverzekering | GBL_SSV_* (7 types), account_movements (+ appendix + letter), account_state, amendment, bank_transfer_form, certificate (+ frontpage), contract, eid21/eid26, general_conditions, invoice_state, transaction (+ extended) | Ja | Nee | Nee | 20+ includes (EID/SID_costs, account_features, fund_details, guarantee_details, etc.) | 5 XMP files | Actief  - tweede meest complex |
| 17 | NewHyp | Nieuwe Hypotheek | HSB_NHY_*, advance, agreement, conditional_discount, esis, general_conditions, role_signatures, signatures | Ja | Nee | Nee | 15+ includes (annual_percentage_rate, credit_insurance_esis, loan_schedule, etc.) | Nee | Actief |
| 18 | Patrimonial_Invest | Patrimoniaal | certificate | Ja | Nee | Nee | Nee | Nee | Beperkt |
| 19 | Patrimonial_Invest_Premium | Patrimoniaal Premium | certificate | Ja | Nee | Nee | Nee | Nee | Beperkt |
| 20 | Patronale_Life_Flexible | Flexibel | certificate, contract, eid, ng, sid | Ja | ng_67 | 67 | Nee | Nee | Actief |
| 21 | Roerend | Roerend krediet | advance, agreement, general_conditions, secci | Ja | Nee | Nee | 6 includes (advance_composition, annual_percentage_rate, etc.) | Nee | Actief |
| 22 | Secure_21 | Veilig Tak 21 | account_movements, account_state, certificate, contract, eid | Ja | Nee | Nee | Nee | Nee | Actief |
| 23 | Short_Term_Cover | Korte termijn | agreement_first_page, bank_transfer_form, checklist, contract, financial_info, general_conditions, proposal | Ja | Nee | Nee | 10+ includes (bank_transfer, broker, contract_roles, etc.) | Nee | Actief |
| 24 | Wet4892 | Wettelijk (4892) | GBL_HYP_*, SKM_HYP_*, advance, agreement, decision (+ summary), dossier_summary, esis, first-notice (+ new/old), general_conditions, income_*, loan-completion, notice-of-default, offer_summary, registered-notice, signing-agent-settlement | Ja | Nee | Nee | 15+ includes (assets_mortgage, conditional_discount, loan_schedule variants, etc.) | Nee | Actief  - derde meest complex |

---

## Shared Includes (templates/includes/)

Globale includes die gedeeld worden over meerdere productlijnen:

| Include | Beschrijving | Gebruikt door |
|---------|-------------|--------------|
| html_head_nl_BE / html_head_fr_BE | HTML header met meta-tags, logo, print-settings | Alle producten |
| recipient-header.html | Adresblok voor brieven (custom_address support) | Generic, GenericLoan, Life_Insurance |
| recipient.html | Inline adresweergave | Meerdere producten |
| custom_macros.html | Helper macro's (join_names) | Meerdere producten |
| broker.html / broker_details.html | Makelaarsinformatie | HypoSelect, Short_Term_Cover, Investeringskrediet |
| signatures.html | Handtekeningblokken | GenericLoan, Life_Insurance |
| loan_schedule_nl_BE / loan_schedule_fr_BE | Aflossingsplan | NewHyp, Wet4892, Investeringskrediet |
| coverage_nl_BE / coverage_fr_BE | Dekkingsoverzicht | HypoSelect, Short_Term_Cover |
| pep_BE / pep_nl_BE | Politically Exposed Persons check | Credit_Insurance, HypoSelect |
| sepa_mandate_BE.html | SEPA mandaat | Credit_Insurance, GenericLoan |

---

## Base Templates (templates/base/)

| Bestand | Type | Beschrijving |
|---------|------|-------------|
| base_template.xml | DOCX | Office Open XML base met Jinja blocks (body, coverpage). ~158KB |
| certificate_nl_BE.xml | DOCX | Certificaat base voor NL. ~358KB |
| certificate_fr_BE.xml | DOCX | Certificaat base voor FR |

---

## Installatie Templates (templates/installation_templates/)

Referentie-templates van vintage 1210 met eigen mappenstructuur:
- `documents/`  - ConsumerLoan, Generic, GenericInsurance, GenericLoan, LifeInsurance, MaterialDamage, Wet23062016, Wet4892
- `financial/`  - agreement_verification_form, product_summary, transaction_verification_form
- `includes/`  - 60+ shared partials
- `macros/html.html`  - Core render macro's (render_table, render_td, render_title_table, etc.)
- `notifications/`  - Per product (ConsumerLoan, Generic, etc.)

---

## Notifications (templates/notifications/)

Notificatie-templates per product (26 productmappen), elk met NL/FR varianten voor:
- Agreements, certificates, standard letters, account movements

---

## Observaties & Aandachtspunten

1. **Duplicatie**: Veel productlijnen (Generic21, Generic23, Generic44, Fix_21, Secure_21, FructiStarSafe21) delen bijna identieke template-structuren  - kandidaten voor consolidatie via Jinja inheritance.
2. **Complexiteit**: GenericLoan (35+ templates, 20+ includes), Life_Insurance (30+ templates, 20+ includes, 5 XMP), en Wet4892 (25+ templates, 15+ includes) zijn de meest complexe productlijnen.
3. **REGData/SIData**: Alleen Boutique_23, Evolis, en Patronale_Life_Flexible hebben deze subdirectories. Elk paar (ng_XXX) bestaat in NL en FR variant.
4. **XMP metadata**: Alleen Credit_Insurance en Life_Insurance hebben XMP-bestanden. Andere producten missen deze  - potentieel compliance-risico.
5. **Naamgeving**: Inconsistent  - sommige bestanden gebruiken underscore (account_movements), andere kebab-case (first-notice), en sommige camelCase (GenericLoan).
6. **Legacy**: installation_templates/vintage 1210 bevat een oudere versie van het systeem met eigen macro's en structuur. Dient als referentie maar is niet actief in gebruik.
