#!/usr/bin/env python3
# Generator voor de ng_xxx REGData/SIData fiches.
#
# Ipv ~100 bijna identieke bestanden met de hand te maken, leest dit script
# de fondsenlijst uit config/ng_funds.json en schrijft per fonds, product en
# taal een klein extends-bestand dat de gedeelde base overschrijft.
#
# Bestaande bestanden worden NIET overschreven (zo blijven handmatige
# aanpassingen staan). Run: python scripts/gen_ng_templates.py

import os
import json

DOCS = "templates/documents"
SHARED = "documents/_shared_boutique"


def reg_template(fund, locale):
    base = "%s/regdata_ng_base_%s.html" % (SHARED, locale)
    out = "{%%- extends '%s' -%%}\n\n" % base
    out += "{%% block fund_name %%}%s{%% endblock %%}\n" % fund["name"]
    out += "{%% block fund_code %%}%s{%% endblock %%}\n" % fund["code"]
    out += "{%% block isin %%}%s{%% endblock %%}\n" % fund["isin"]
    if fund.get("duration"):
        out += "{% block extra_rows %}\n"
        out += '    <tr><td class="label">Duration</td><td>%s</td></tr>\n' % fund["duration"]
        out += "{% endblock %}\n"
    return out


def si_template(fund, locale):
    # sidata base bestaat voorlopig enkel in NL, FR valt voorlopig terug op
    # de NL base. TODO: aparte FR sidata base in sprint 3 cleanup
    base = "%s/sidata_ng_base_nl_BE.html" % SHARED
    out = "{%%- extends '%s' -%%}\n\n" % base
    out += "{%% block fund_name %%}%s{%% endblock %%}\n" % fund["name"]
    out += "{%% block sri %%}%s{%% endblock %%}\n" % fund["sri"]
    out += "{%% block ongoing_costs %%}{{ %s|format_percentage }}{%% endblock %%}\n" % fund["ongoing_costs"]
    return out


def write_if_new(path, content):
    if os.path.exists(path):
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    return True


def main():
    cfg = json.load(open("config/ng_funds.json", encoding="utf-8"))
    made = 0
    skipped = 0

    for product in cfg["products"]["REGData"]:
        for fund in cfg["funds"]:
            for locale in ("nl_BE", "fr_BE"):
                path = "%s/%s/REGData/%s_%s.html" % (DOCS, product, fund["code"], locale)
                if write_if_new(path, reg_template(fund, locale)):
                    made += 1
                else:
                    skipped += 1

    for product in cfg["products"]["SIData"]:
        for fund in cfg["funds"]:
            for locale in ("nl_BE", "fr_BE"):
                path = "%s/%s/SIData/%s_%s.html" % (DOCS, product, fund["code"], locale)
                if write_if_new(path, si_template(fund, locale)):
                    made += 1
                else:
                    skipped += 1

    print("aangemaakt: %d, overgeslagen (bestond al): %d" % (made, skipped))


if __name__ == "__main__":
    main()
