# Taal-routerbug: dossiertaal van de verkeerde rolhouder (US-06)

## Symptoom
Een Franstalige klant kreeg soms een Nederlandstalig document. De taalkeuze klopte niet in
dossiers met meerdere betrokkenen (bv. verzekeringnemer + medeverzekerde of een tegenpartij).

## Oorzaak
De dossiertaal werd afgeleid door de recipients te groeperen en de eerste te nemen:

```jinja
{% set language = (group_recipients | first).language %}
```

`group_recipients` sorteert echter op de adres-tuple, niet op rol. `| first` gaf dus de
**gesorteerd-eerste** recipient, en dat is niet noodzakelijk de **primaire rolhouder**
(de verzekeringnemer). In een gemengd NL/FR-dossier bepaalde daardoor soms een neventegenpartij
de taal, met een NL-brief voor een FR-klant als gevolg.

Deze gotcha staat niet in de vendor-documentatie; `group_recipients` zelf is wel gedocumenteerd
(VFIN-3042), maar niet dat de sortering op adres gebeurt.

## Fix
De taal moet van de **primaire rolhouder** komen. In vFinance is het idioom:

```jinja
{% set language = (first_role | group_recipients).language | from_list(['nl_BE', 'fr_BE'], 'nl_BE') %}
```

`first_role` neemt eerst de primaire rol (verzekeringnemer), en pas daarna wordt gegroepeerd. De
`from_list`-selector valt terug op `nl_BE` als er geen geldige taal is.

## Toepassing in deze repo
In de gedeelde movements-base (`documents/Life_Insurance/account_movements_BE.html`) wordt de taal
nu bepaald vanuit de primaire rol via de `roles`-lijst (eerste rol = primaire rolhouder), met een
terugval op `recipient.language`:

```jinja
{% set primary_role = roles | first if roles else none %}
{% set language = (primary_role.language if primary_role and primary_role.language
                   else recipient.language) | from_list(['nl_BE', 'fr_BE'], 'nl_BE') %}
```

## Testgeval
Dossier met een FR-verzekeringnemer (rol 1) en een NL-medeverzekerde (rol 2) waarvan het adres
alfabetisch vóór dat van de verzekeringnemer komt:

- **Voor de fix:** `group_recipients | first` -> NL-medeverzekerde -> document in het Nederlands (fout).
- **Na de fix:** primaire rol (FR-verzekeringnemer) -> document in het Frans (correct).
