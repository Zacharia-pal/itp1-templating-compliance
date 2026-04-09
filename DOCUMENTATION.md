# Template Documentatie

## Render Stack

### HTML Pipeline
Templates worden gerenderd via een HTML pipeline die Jinja2 gebruikt:

```
base template (layout)
  -> block html_head (meta-tags, print settings, logo, QR)
  -> block content (document body)
     -> block letter_main / product-specifieke blocks
```

### DOCX Pipeline
Voor Word-documenten wordt Office Open XML gebruikt:

```
base/base_template.xml (package skeleton)
  -> block body (document inhoud)
  -> footer met compliance info en templates_revision()
```

## Macro Library

Alle macro's worden geimporteerd uit `macros/html.html`:

- `render_table()` - Tabel met optionele class
- `render_td()` - Tabelcel met optionele class, width, colspan
- `render_title_table()` - Titeltabel
- `render_todo_font()` - TODO-markering
- `render_tbd_font()` - TBD-markering
- `hypo_header()` - Hypothecaire document header

Gebruik: `{%- import 'macros/html.html' as html with context -%}`

## Custom Filters

vFinance biedt de volgende custom Jinja filters:

| Filter | Beschrijving | Voorbeeld |
|--------|-------------|-----------|
| `get_setting` | Haal setting op uit settings dict | `'LOGO'\|get_setting(settings)` |
| `format_currency` | Bedrag formatteren | `amount\|format_currency` |
| `format_date` | Datum formatteren | `date\|format_date` |
| `format_datetime` | Datum+tijd formatteren | `now\|format_datetime` |
| `convert_stored_image` | Base64 image conversie | `logo\|convert_stored_image` |
| `append_locale` | Locale suffix toevoegen | `code\|append_locale()` |
| `raise_user_exception` | Foutmelding gooien | `msg\|raise_user_exception` |

## Template Blocks

### Standaard blocks in HTML templates:

- `html_head` - Meta-tags voor print (logo, QR, headers, title)
- `content` - Hoofdinhoud van het document
- `letter_main` - Briefinhoud (binnen content)
- `letter_content` - Vrije tekst van de brief
- `letter_signature` - Handtekeningblok
- `subject` - Onderwerpregel

### Product-specifieke blocks:

Sommige producten definiiren eigen blocks, bijv:
- `coverpage` - Voorpagina (certificaten)
- `packages` - Pakketoverzicht (certificaten)

## Directory Atlas

| Map | Inhoud |
|-----|--------|
| `base/` | XML base templates voor DOCX pipeline |
| `documents/` | Product-specifieke document templates |
| `includes/` | Gedeelde includes (headers, recipient, signatures) |
| `notifications/` | Notificatie wrappers per product |
| `partials/` | Herbruikbare XML partials |
| `time_deposit/` | Termijndeposito templates |
| `images/` | Logo's en branding assets |
| `installation_templates/` | Referentie templates (vintage 1210) |

## Localisatie

- Bestandsnamen: `template_nl_BE.html` / `template_fr_BE.html`
- Runtime vertaling: `{{ _('Subject') }}` (Jinja i18n)
- Conditionele metadata: `NOTIFICATION_HEADER_1_nl_BE` vs `_fr_BE`
- Macro's: `join_names(items, 'nl_BE')` voor taalspecifieke voegwoorden

## Extension Guide

### Nieuw document toevoegen:

1. Maak `documents/ProductNaam/document_nl_BE.html` aan
2. Extend de juiste base: `{%- extends 'documents/Generic/empty_letter_BE.html' -%}`
3. Vul de blocks in: `html_head`, `letter_content`, etc.
4. Maak de FR variant: `document_fr_BE.html`
5. Update `TEMPLATE_REGISTRY.json`
6. Update `COMPAT_MATRIX.md`

### Nieuwe macro toevoegen:

1. Voeg toe aan `macros/html.html`
2. Import in templates: `{%- import 'macros/html.html' as html with context -%}`
3. Documenteer in dit bestand
