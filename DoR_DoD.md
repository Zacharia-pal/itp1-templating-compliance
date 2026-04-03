# Definition of Ready (DoR) & Definition of Done (DoD)

## Definition of Ready

Een user story is **Ready** wanneer:

1. **Duidelijke beschrijving**: De user story volgt het formaat "Als [rol] wil ik [actie] zodat [waarde]"
2. **Acceptatiecriteria**: Er zijn concrete, testbare acceptatiecriteria gedefinieerd
3. **Afhankelijkheden**: Alle externe afhankelijkheden (Erwin/Eduardo input, vFinance versie-info) zijn opgehelderd
4. **Schatting**: De story is geschat in uren en past binnen de sprint
5. **Template-specifiek**: Voor migratie-stories is het bronbestand (visueel XML) geïdentificeerd en de doelstructuur (Jinja HTML) bepaald
6. **Locale-compleet**: Beide taalvarianten (nl_BE en fr_BE) zijn meegenomen in de scope

## Definition of Done

Een user story is **Done** wanneer:

### Voor template-migratie stories:
- [ ] Template is gemigreerd van visueel XML naar Jinja HTML
- [ ] Jinja inheritance is correct opgezet (`{% extends %}`, `{% block %}`)
- [ ] Beide taalvarianten (nl_BE, fr_BE) zijn aanwezig en correct
- [ ] XMP metadata (indien van toepassing) is via XML-includes in `<head>` opgenomen
- [ ] Template is opgenomen in TEMPLATE_REGISTRY.json met correcte metadata
- [ ] Template is opgenomen in COMPAT_MATRIX.md met vintage-compatibiliteit
- [ ] Geen hardcoded visuele XML-elementen meer aanwezig (geen `<w:...>` tags in HTML templates)
- [ ] Custom filters (`get_setting`, `format_currency`, `format_date`) worden correct gebruikt
- [ ] Commit message volgt conventie (`feat:`, `fix:`, `docs:`, etc.)

### Voor automatisering stories:
- [ ] Workflow/script is functioneel en gedocumenteerd
- [ ] Secrets zijn niet hardcoded (gebruik `${{ secrets.XXX }}`)
- [ ] Error handling is aanwezig voor API-calls (JIRA, GitHub, Microsoft Graph)
- [ ] Concurrency is afgehandeld (geen duplicate runs)
- [ ] Tweetalig waar van toepassing (NL/FR)

### Voor documentatie stories:
- [ ] Document is geschreven in Markdown
- [ ] Document is opgenomen in de juiste directory (`docs/`)
- [ ] Cross-references naar gerelateerde documenten zijn correct
- [ ] Geen bedrijfsgevoelige informatie (API keys, persoonlijke data) in het document

### Algemeen (alle stories):
- [ ] Code/documentatie is gecommit naar de juiste branch
- [ ] Relevante wijzigingen zijn besproken met mentor (Eduardo/Erwin)
- [ ] Time registration is bijgewerkt in projectwerk.vives.be
