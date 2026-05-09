#!/usr/bin/env python3
"""
RigSize Live marketing site - build script.

Genereert 6 statische HTMLs uit template.html + translations/*.json.

Usage:
    python3 build.py

Output:
    index.html       (NL, root)
    en/index.html
    de/index.html
    fr/index.html
    es/index.html
    it/index.html
"""

import json
import os
import re
import sys
from pathlib import Path

LANGUAGES = ['nl', 'en', 'de', 'fr', 'es', 'it']
DEFAULT_LANG = 'nl'
ROOT = Path(__file__).parent.resolve()

PLACEHOLDER_RE = re.compile(r'\{\{([a-zA-Z0-9_.]+)\}\}')


def load_translations(lang):
    path = ROOT / 'translations' / f'{lang}.json'
    if not path.exists():
        print(f'FOUT: vertaling ontbreekt: {path}')
        sys.exit(1)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def flatten(d, parent_key='', sep='.'):
    """Flatten nested dict: {'a': {'b': 'x'}} -> {'a.b': 'x'}"""
    items = {}
    for k, v in d.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.update(flatten(v, new_key, sep))
        else:
            items[new_key] = v
    return items


def render(template, translations_flat, lang):
    """Replace {{KEY}} placeholders with translations and set lang attribute."""
    missing = []

    def repl(match):
        key = match.group(1).lower().replace('_', '.')
        # Also try uppercase variant lookup
        if key in translations_flat:
            return str(translations_flat[key])
        # Try original casing as-is (no transform)
        raw_key = match.group(1)
        if raw_key in translations_flat:
            return str(translations_flat[raw_key])
        # Try lowercase version
        if raw_key.lower() in translations_flat:
            return str(translations_flat[raw_key.lower()])
        missing.append(raw_key)
        return match.group(0)  # Leave placeholder if not found

    out = PLACEHOLDER_RE.sub(repl, template)

    # Set HTML lang attribute
    out = re.sub(r'<html\s+lang="[^"]*"', f'<html lang="{lang}"', out, count=1)

    if missing:
        unique_missing = sorted(set(missing))
        print(f'  WAARSCHUWING [{lang}]: {len(unique_missing)} ontbrekende keys:')
        for k in unique_missing[:10]:
            print(f'    - {k}')
        if len(unique_missing) > 10:
            print(f'    ... en {len(unique_missing) - 10} meer')

    return out


def main():
    template_path = ROOT / 'template.html'
    if not template_path.exists():
        print(f'FOUT: template.html ontbreekt: {template_path}')
        sys.exit(1)

    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    print('=== RSL marketing build ===')
    print(f'Template: {template_path}')
    print(f'Talen: {", ".join(LANGUAGES)}')
    print('')

    for lang in LANGUAGES:
        print(f'[{lang}] genereren...')
        translations = load_translations(lang)
        translations_flat = flatten(translations)
        html = render(template, translations_flat, lang)

        if lang == DEFAULT_LANG:
            out_path = ROOT / 'index.html'
        else:
            out_dir = ROOT / lang
            out_dir.mkdir(exist_ok=True)
            out_path = out_dir / 'index.html'

        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)

        rel = out_path.relative_to(ROOT)
        size_kb = out_path.stat().st_size / 1024
        print(f'  -> {rel} ({size_kb:.1f} KB)')

    print('')
    print('=== Klaar ===')
    print('Test lokaal: python3 -m http.server 8000')
    print('Daarna: http://localhost:8000  (NL)')
    print('        http://localhost:8000/en  (EN)  enz.')


if __name__ == '__main__':
    main()
