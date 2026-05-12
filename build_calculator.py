#!/usr/bin/env python3
"""
build_calculator.py
Generates per-language HTML pages for the Vin & Foil Calculator.

Reads:
  calculator-template.html
  translations/calculator-{lang}.json  (one per language)

Writes (per language):
  {path}/{slug}/index.html

Run from the repo root:
  cd ~/rigsizelive-marketing && python3 build_calculator.py
"""

import json
import os
import re
import sys

# SITE config
SITE_URL = "https://www.rigsizelive.com"

# Language config - SEO-optimized URL slugs per language
LANGUAGES = [
    {"code": "nl", "slug": "vin-foil-calculator",        "path": "",     "hreflang": "nl",     "home": "/"},
    {"code": "en", "slug": "fin-foil-calculator",        "path": "en/",  "hreflang": "en",     "home": "/en/"},
    {"code": "de", "slug": "finnen-foil-rechner",        "path": "de/",  "hreflang": "de",     "home": "/de/"},
    {"code": "fr", "slug": "calculateur-aileron-foil",   "path": "fr/",  "hreflang": "fr",     "home": "/fr/"},
    {"code": "es", "slug": "calculadora-aleta-foil",     "path": "es/",  "hreflang": "es",     "home": "/es/"},
    {"code": "it", "slug": "calcolatore-pinna-foil",     "path": "it/",  "hreflang": "it",     "home": "/it/"},
]
DEFAULT_LANG = "nl"


def load_translations(repo_root, lang_code):
    """Load translations for given language. Returns None if not available."""
    path = os.path.join(repo_root, "translations", f"calculator-{lang_code}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_translation(translations, key, default=None):
    """Case-insensitive flat-key lookup."""
    if key in translations:
        return translations[key]
    key_lower = key.lower()
    for k, v in translations.items():
        if k.lower() == key_lower:
            return v
    return default


def url_for_lang(lang):
    """Full canonical URL for a language config."""
    return f"{SITE_URL}/{lang['path']}{lang['slug']}/"


def build_hreflang_tags(current_lang):
    """Generate alternate hreflang link tags for all languages + x-default."""
    tags = []
    for lang in LANGUAGES:
        tags.append(
            f'<link rel="alternate" hreflang="{lang["hreflang"]}" href="{url_for_lang(lang)}" />'
        )
    # x-default points to NL (default language)
    default = next(l for l in LANGUAGES if l["code"] == DEFAULT_LANG)
    tags.append(
        f'<link rel="alternate" hreflang="x-default" href="{url_for_lang(default)}" />'
    )
    return "\n".join(tags)


FLAG_NAME = {
    "nl": ("🇳🇱", "Nederlands"),
    "en": ("🇬🇧", "English"),
    "de": ("🇩🇪", "Deutsch"),
    "fr": ("🇫🇷", "Français"),
    "es": ("🇪🇸", "Español"),
    "it": ("🇮🇹", "Italiano"),
}


def build_lang_switcher_links(current_code):
    """Desktop lang switcher menu links."""
    out = []
    for lang in LANGUAGES:
        flag, name = FLAG_NAME[lang["code"]]
        out.append(
            f'          <a href="{url_for_lang(lang)}" data-lang="{lang["code"]}">{flag} {name}</a>'
        )
    return "\n".join(out)


def build_mobile_lang_links(current_code):
    """Mobile menu lang links (same as desktop but indented differently)."""
    out = []
    for lang in LANGUAGES:
        flag, name = FLAG_NAME[lang["code"]]
        active = " class=\"active\"" if lang["code"] == current_code else ""
        out.append(
            f'    <a href="{url_for_lang(lang)}" data-lang="{lang["code"]}"{active}>{flag} {name}</a>'
        )
    return "\n".join(out)


def build_faq_html(faq_items):
    """Render FAQ items as <details> blocks."""
    parts = []
    for i, item in enumerate(faq_items):
        is_open = " open" if i == 0 else ""
        # Escape HTML special chars in q/a
        q = item["q"]
        a = item["a"]
        parts.append(
            f'      <details class="faq-item"{is_open}>\n'
            f'        <summary>{q}</summary>\n'
            f'        <p>{a}</p>\n'
            f'      </details>'
        )
    return "\n".join(parts)


def build_faq_schema(faq_items):
    """Render FAQ items as Schema.org JSON-LD entities (inside FAQPage mainEntity)."""
    entities = []
    for item in faq_items:
        # JSON-encode to handle quotes/specials properly
        q_json = json.dumps(item["q"], ensure_ascii=False)
        a_json = json.dumps(item["a"], ensure_ascii=False)
        entities.append(
            '{'
            '"@type":"Question",'
            f'"name":{q_json},'
            '"acceptedAnswer":{'
            '"@type":"Answer",'
            f'"text":{a_json}'
            '}'
            '}'
        )
    return ",".join(entities)


def build_calc_i18n_json(translations):
    """Build the i18n object that gets inlined into the calculator's JS."""
    obj = {
        "SAIL":           get_translation(translations, "calc.sail", ""),
        "SAIL_PH":        get_translation(translations, "calc.sail_ph", ""),
        "WING_SIZE":      get_translation(translations, "calc.wing_size", ""),
        "WING_PH":        get_translation(translations, "calc.wing_ph", ""),
        "WIND":           get_translation(translations, "calc.wind", ""),
        "RIDER":          get_translation(translations, "calc.rider", ""),
        "WIND_LOW":       get_translation(translations, "calc.wind_low", ""),
        "WIND_MID":       get_translation(translations, "calc.wind_mid", ""),
        "WIND_HIGH":      get_translation(translations, "calc.wind_high", ""),
        "RIDER_LIGHT":    get_translation(translations, "calc.rider_light", ""),
        "RIDER_ALLROUND": get_translation(translations, "calc.rider_allround", ""),
        "RIDER_STRONG":   get_translation(translations, "calc.rider_strong", ""),
        "RES_STD":        get_translation(translations, "calc.res_std", ""),
        "RES_STD_SUB":    get_translation(translations, "calc.res_std_sub", ""),
        "RES_PERF":       get_translation(translations, "calc.res_perf", ""),
        "RES_PERF_SUB":   get_translation(translations, "calc.res_perf_sub", ""),
        "WARN_MAX":       get_translation(translations, "calc.warn_max", ""),
        "WARN_MIN":       get_translation(translations, "calc.warn_min", ""),
        "WARN_FOIL_WIDE": get_translation(translations, "calc.warn_foil_wide", ""),
        "BEGINNER":       get_translation(translations, "calc.beginner", ""),
        "INTERMEDIATE":   get_translation(translations, "calc.intermediate", ""),
        "ADVANCED":       get_translation(translations, "calc.advanced", ""),
        "LEVEL":          get_translation(translations, "calc.level", ""),
        "FUSELAGE":       get_translation(translations, "calc.fuselage", ""),
        "MAST":           get_translation(translations, "calc.mast", ""),
        "FOIL_NOTE":      get_translation(translations, "calc.foil_note", ""),
    }
    return json.dumps(obj, ensure_ascii=False)


def render_template(template, translations, lang_cfg):
    """Replace all {{PLACEHOLDER}} tokens with values from translations."""
    result = template

    # Computed/derived placeholders FIRST (before generic placeholder pass)
    canonical = url_for_lang(lang_cfg)
    home_url = f"{SITE_URL}{lang_cfg['home']}"

    faq_items = get_translation(translations, "faq.items", [])
    faq_html = build_faq_html(faq_items)
    faq_schema_items = build_faq_schema(faq_items)

    computed = {
        "LANG_CODE":             lang_cfg["hreflang"],
        "CANONICAL_URL":         canonical,
        "HREFLANG_TAGS":         build_hreflang_tags(lang_cfg["code"]),
        "HOME_URL":              home_url,
        "LANG_SWITCHER_LINKS":   build_lang_switcher_links(lang_cfg["code"]),
        "MOBILE_LANG_LINKS":     build_mobile_lang_links(lang_cfg["code"]),
        "FAQ_ITEMS_HTML":        faq_html,
        "FAQ_SCHEMA_ITEMS":      faq_schema_items,
        "CALC_I18N_JSON":        build_calc_i18n_json(translations),
    }

    # First pass: replace computed placeholders (these are case-sensitive uppercase)
    for key, val in computed.items():
        result = result.replace("{{" + key + "}}", str(val))

    # Second pass: replace translation placeholders (case-insensitive)
    pattern = re.compile(r"\{\{([A-Za-z][A-Za-z0-9._]+)\}\}")
    def replace_token(match):
        key = match.group(1)
        val = get_translation(translations, key)
        if val is None:
            print(f"  WARN: missing translation for {{{{ {key} }}}}", file=sys.stderr)
            return match.group(0)  # keep placeholder visible for debugging
        return str(val)
    result = pattern.sub(replace_token, result)

    return result


def main():
    repo_root = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(repo_root, "calculator-template.html")

    if not os.path.exists(template_path):
        print(f"ERROR: {template_path} not found")
        sys.exit(1)

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    built = 0
    skipped = 0
    for lang_cfg in LANGUAGES:
        translations = load_translations(repo_root, lang_cfg["code"])
        if translations is None:
            print(f"SKIP {lang_cfg['code']}: translations/calculator-{lang_cfg['code']}.json not found")
            skipped += 1
            continue

        html = render_template(template, translations, lang_cfg)

        out_dir = os.path.join(repo_root, lang_cfg["path"].rstrip("/"), lang_cfg["slug"]) if lang_cfg["path"] else os.path.join(repo_root, lang_cfg["slug"])
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        # Calculate relative path for nicer logging
        rel = os.path.relpath(out_path, repo_root)
        print(f"OK  {lang_cfg['code']}: {rel}")
        built += 1

    print(f"\nDone: {built} built, {skipped} skipped (no translation file yet)")


if __name__ == "__main__":
    main()
