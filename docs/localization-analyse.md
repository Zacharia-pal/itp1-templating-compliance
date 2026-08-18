# Localization-analyse en ontwerp (US-01)

Analyse van de huidige per-taal-aanpak van de account_movements-brieven en het ontwerp van het
canonieke from_list-taalpatroon voor de FF-148 -> Release-2 migratie.

## 1. Inventaris (ST-01a)

Alle account_movements-templates staan per taal in een apart bestand (`_nl_BE` / `_fr_BE`).
Zes producten, telkens een paar:

| Product | NL | FR | Extend |
|---|---|---|---|
| Life_Insurance | account_movements_nl_BE.html | account_movements_fr_BE.html | `_shared/_base_letter.html` (de base) |
| Boutique_23 | account_movements_nl_BE.html | account_movements_fr_BE.html | Life_Insurance |
| Generic21 | account_movements_nl_BE.html | account_movements_fr_BE.html | Life_Insurance |
| Generic23 | account_movements_nl_BE.html | account_movements_fr_BE.html | Life_Insurance |
| Generic44 | account_movements_nl_BE.html | account_movements_fr_BE.html | Life_Insurance |
| Short_Term_Cover | account_movements_nl_BE.html | account_movements_fr_BE.html | Life_Insurance |

Totaal 12 bestanden. Life_Insurance is de base met de volledige body; de andere vijf producten
overschrijven enkel het `html_head`-block (document_code, html_head-include, print-title).

## 2. Wat verschilt er per taal?

Als je de NL- en FR-variant naast elkaar legt (bv. Life_Insurance), is de structuur identiek. Enkel
dit verschilt:

- **Locale-suffix in document_code**: `%s.MOV.nl_BE` vs `%s.MOV.fr_BE`.
- **html_head-include**: `includes/html_head_nl_BE.html` vs `includes/html_head_fr_BE.html`.
- **print-title**: "Rekeningbewegingen" vs "Mouvements de compte".
- **subject-tekst**: vertaalde onderwerpregel.
- **letter_content-labels**: kolomkoppen (Datum/Date, Omschrijving/Libelle, ...) en de aanhef.

De tabellogica (`for mv in movements`, `be_amount`, tfoot) is in beide talen exact hetzelfde.
Dat is precies de duplicatie die release 148 wil wegwerken: 1 template, taal als parameter.

## 3. Ontwerp: canoniek from_list-taalpatroon (ST-01b)

### Doel (uit de vendor-migratiegids 13.1.1.8.1 / VFIN-2309)
De per-taal-bestanden vervangen door 1 unsuffixed template die de taal runtime bepaalt via de
`from_list`-selector en de taalspecifieke stukken dynamisch includeert.

### Taalbepaling
De dossiertaal komt van de ontvanger, met een default als er niets gezet is:

```jinja
{% set language = recipient.language | from_list(['nl_BE', 'fr_BE'], 'nl_BE') %}
```

`from_list` neemt de taal van de recipient als die in de lijst zit, anders de default (`nl_BE`).
De taal wordt eenmaal bovenaan bepaald en in de rest van de template hergebruikt (with-scope).

### Structuur van de unified template
Een unsuffixed `account_movements_BE.html` die:

1. `_shared/_base_letter.html` extend.
2. `language` bovenaan zet met de from_list-selector.
3. In `block html_head` de taalspecifieke head dynamisch includeert en de document_code met de
   juiste suffix zet:

```jinja
{% block html_head %}
    {% set document_code = '%s.MOV.%s' | format(productcode, language) %}
    {% set xmp_template = 'documents/Life_Insurance/xmp/contract.xml' %}
    {% include 'includes/html_head_%s.html' | format(language) %}
{% endblock %}
```

4. De taalspecifieke tekst (subject + body-labels) uit een per-taal body-include haalt:

```jinja
{% block subject %}{% include 'documents/Life_Insurance/_movements_subject_%s.html' | format(language) %}{% endblock %}
{% block letter_content %}{% include 'documents/Life_Insurance/_movements_body_%s.html' | format(language) %}{% endblock %}
```

Dynamische includes zijn al in gebruik in de codebase (`{% include xmp_template %}` in de
html_head-includes), dus dit past in het bestaande patroon.

### Niet-destructieve aanpak
De bestaande `_nl_BE` / `_fr_BE` bestanden blijven staan tot na de render-test. Zo kan de output
van de unified template vergeleken worden met de oude output voor we iets verwijderen. Opkuisen
gebeurt pas na akkoord (buiten deze sprint).

### Uitrol
- US-02: het patroon opzetten op Life_Insurance/Boutique_23 (base + eerste product).
- US-03: uitrol naar de Generic-familie (Generic21/23/44).
- US-04: Short_Term_Cover, en de gemigreerde set noteren in de registry.

## 4. Aandachtspunten
- De taal-routerbug (US-06): `recipient` moet de primaire rolhouder zijn, niet de gesorteerd-eerste.
  Bij het bepalen van `recipient.language` letten we hierop (zie US-06).
- De print-title zit nu in het html_head-block; die verhuist mee naar de per-taal head-include of
  de body-include zodat er geen NL-tekst achterblijft in de FR-render.
