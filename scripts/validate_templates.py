#!/usr/bin/env python3
# Template validatie voor de CI. Loopt over alle templates en checkt:
#   1. parset de template zonder syntax error?
#   2. bestaan de templates waarnaar extends/include verwijst?
#
# Rendert niet echt (geen data), het gaat om kapotte structuur vroeg vangen.
# Een verkeerde extends pad (zoals de offer_summary FR bug in Sprint 1) valt
# zo meteen op ipv pas bij het genereren.

import os
import sys

from jinja2 import Environment, FileSystemLoader, TemplateSyntaxError
from jinja2 import meta

ROOT = "templates"


def all_templates(env):
    out = []
    for name in env.list_templates(extensions=("html", "xml")):
        out.append(name)
    return out


def check(env, name):
    problems = []
    try:
        src = env.loader.get_source(env, name)[0]
        ast = env.parse(src)
    except TemplateSyntaxError as e:
        return ["syntax error: %s (regel %s)" % (e.message, e.lineno)]

    # referenced_templates geeft de extends/include/import targets
    refs = meta.find_referenced_templates(ast)
    known = set(env.list_templates(extensions=("html", "xml")))
    for ref in refs:
        if ref is None:
            # dynamische include ({% include var %}), kunnen we niet checken
            continue
        if ref not in known:
            problems.append("verwijst naar onbestaande template: %s" % ref)
    return problems


def main():
    env = Environment(loader=FileSystemLoader(ROOT))
    names = all_templates(env)
    print("gevonden templates:", len(names))

    failed = 0
    for name in sorted(names):
        problems = check(env, name)
        if problems:
            failed += 1
            print("[FAIL]", name)
            for p in problems:
                print("       -", p)

    if failed:
        print("\n%d template(s) met problemen" % failed)
        sys.exit(1)
    print("\nalle templates ok")


if __name__ == "__main__":
    main()
