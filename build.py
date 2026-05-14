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

# Site root URL (for canonical, hreflang, sitemap)
SITE_URL = 'https://www.rigsizelive.com'

# Calculator URLs per taal (gegenereerd door build_calculator.py)
# Pas hier aan als de calculator-slugs wijzigen.
CALC_SLUGS = {
    'nl': 'vin-foil-calculator',
    'en': 'en/fin-foil-calculator',
    'de': 'de/finnen-foil-rechner',
    'fr': 'fr/calculateur-aileron-foil',
    'es': 'es/calculadora-aleta-foil',
    'it': 'it/calcolatore-pinna-foil',
}

# Flag emoji + nice name per taal (voor hreflang/discovery, sitemap is taal-agnostic)
LANG_HREFLANG = {
    'nl': 'nl',
    'en': 'en',
    'de': 'de',
    'fr': 'fr',
    'es': 'es',
    'it': 'it',
}
# Hardcoded labels per taal (geen JSON keys nodig voor deze)
NEXT_LABELS = {
    'nl': 'Volgende',
    'en': 'Next',
    'de': 'Weiter',
    'fr': 'Suivant',
    'es': 'Siguiente',
    'it': 'Avanti',
}
END_LABELS = {
    'nl': 'Einde',
    'en': 'End',
    'de': 'Ende',
    'fr': 'Fin',
    'es': 'Fin',
    'it': 'Fine',
}

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


def homepage_url(lang):
    """Canonical URL voor de homepage van een taal."""
    if lang == DEFAULT_LANG:
        return f'{SITE_URL}/'
    return f'{SITE_URL}/{lang}/'


def calc_url(lang):
    """URL voor de calculator-pagina van een taal."""
    slug = CALC_SLUGS.get(lang)
    if not slug:
        return f'{SITE_URL}/'
    return f'{SITE_URL}/{slug}/'


def build_hreflang_tags(current_lang):
    """Genereer alternate hreflang tags voor alle 6 talen + x-default."""
    tags = []
    for lang in LANGUAGES:
        tags.append(
            f'<link rel="alternate" hreflang="{LANG_HREFLANG[lang]}" '
            f'href="{homepage_url(lang)}" />'
        )
    tags.append(
        f'<link rel="alternate" hreflang="x-default" '
        f'href="{homepage_url(DEFAULT_LANG)}" />'
    )
    return '\n'.join(tags)


def render(template, translations_flat, lang):
    """Replace {{KEY}} placeholders with translations and set lang attribute.

    Computed placeholders (added on top of translations_flat):
      - canonical.url: canonical URL voor deze taal-homepage
      - hreflang.tags: alle hreflang link tags
      - calc.url: link naar de calculator-pagina in deze taal
    """
    # Inject computed values into the lookup table (lowercase, dotted)
    computed = {
        'canonical.url': homepage_url(lang),
        'hreflang.tags': build_hreflang_tags(lang),
        'calc.url': calc_url(lang),
    }
    # Build merged lookup: translations win for existing keys; computed adds new keys
    lookup = dict(translations_flat)
    for k, v in computed.items():
        lookup[k] = v

    missing = []

    def repl(match):
        key = match.group(1).lower().replace('_', '.')
        # Also try uppercase variant lookup
        if key in lookup:
            return str(lookup[key])
        # Try original casing as-is (no transform)
        raw_key = match.group(1)
        if raw_key in lookup:
            return str(lookup[raw_key])
        # Try lowercase version
        if raw_key.lower() in lookup:
            return str(lookup[raw_key.lower()])
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


def generate_sitemap():
    """Genereer sitemap.xml met alle 6 homepages en 6 calculator-pagina's,
    inclusief xhtml:link alternates voor multi-language SEO."""
    import datetime
    today = datetime.date.today().isoformat()
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]

    # 6 homepages
    for lang in LANGUAGES:
        url = homepage_url(lang)
        lines.append('  <url>')
        lines.append(f'    <loc>{url}</loc>')
        lines.append(f'    <lastmod>{today}</lastmod>')
        # xhtml:link alternates (homepage variants)
        for alt in LANGUAGES:
            lines.append(
                f'    <xhtml:link rel="alternate" hreflang="{LANG_HREFLANG[alt]}" '
                f'href="{homepage_url(alt)}" />'
            )
        lines.append(
            f'    <xhtml:link rel="alternate" hreflang="x-default" '
            f'href="{homepage_url(DEFAULT_LANG)}" />'
        )
        lines.append('  </url>')

    # 6 calculator pagina's
    for lang in LANGUAGES:
        url = calc_url(lang)
        lines.append('  <url>')
        lines.append(f'    <loc>{url}</loc>')
        lines.append(f'    <lastmod>{today}</lastmod>')
        for alt in LANGUAGES:
            lines.append(
                f'    <xhtml:link rel="alternate" hreflang="{LANG_HREFLANG[alt]}" '
                f'href="{calc_url(alt)}" />'
            )
        lines.append(
            f'    <xhtml:link rel="alternate" hreflang="x-default" '
            f'href="{calc_url(DEFAULT_LANG)}" />'
        )
        lines.append('  </url>')

    lines.append('</urlset>')
    return '\n'.join(lines) + '\n'


def generate_robots():
    """Genereer een schone robots.txt."""
    return (
        'User-agent: *\n'
        'Allow: /\n'
        '\n'
        f'Sitemap: {SITE_URL}/sitemap.xml\n'
    )


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
        # Hardcoded labels per taal voor slider knop
        html = html.replace('__NEXT_LABEL__', NEXT_LABELS.get(lang, 'Next'))
        html = html.replace('__END_LABEL__', END_LABELS.get(lang, 'End'))

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

    # Genereer sitemap.xml (alle 6 homepages + alle 6 calculator-pagina's)
    print('')
    print('[sitemap.xml] genereren...')
    sitemap = generate_sitemap()
    sitemap_path = ROOT / 'sitemap.xml'
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap)
    url_count = sitemap.count('<url>')
    print(f'  -> sitemap.xml ({url_count} URLs)')

    # Genereer robots.txt als die niet bestaat (overschrijft niet)
    robots_path = ROOT / 'robots.txt'
    if not robots_path.exists():
        print('[robots.txt] genereren (nieuw)...')
        with open(robots_path, 'w', encoding='utf-8') as f:
            f.write(generate_robots())
        print(f'  -> robots.txt')
    else:
        print('[robots.txt] bestaat al, overgeslagen')

    print('')
    print('=== Klaar ===')
    print('Test lokaal: python3 -m http.server 8000')
    print('Daarna: http://localhost:8000  (NL)')
    print('        http://localhost:8000/en  (EN)  enz.')


if __name__ == '__main__':
    main()
