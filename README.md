# RigSize Live - Marketing Site

Static multilingual marketing site voor RigSize Live, deployed naar `www.rigsizelive.com` via Vercel.

## Structuur

```
rigsizelive-marketing/
├── template.html              # master template met {{KEY}} placeholders
├── translations/              # vertalingen per taal
│   ├── nl.json                # Nederlands (default)
│   ├── en.json
│   ├── de.json
│   ├── fr.json
│   ├── es.json
│   └── it.json
├── images/                    # alle hero/feature foto's
├── icons/                     # logo's
├── build.py                   # genereert 6 statische HTMLs
├── vercel.json                # Vercel config
│
├── index.html                 # GENERATED: NL versie (root)
├── en/index.html              # GENERATED: EN versie
├── de/index.html              # GENERATED: DE versie
├── fr/index.html              # GENERATED: FR versie
├── es/index.html              # GENERATED: ES versie
└── it/index.html              # GENERATED: IT versie
```

## URLs

| Taal | URL |
|------|-----|
| Nederlands (default) | `www.rigsizelive.com` |
| English | `www.rigsizelive.com/en` |
| Deutsch | `www.rigsizelive.com/de` |
| Francais | `www.rigsizelive.com/fr` |
| Espanol | `www.rigsizelive.com/es` |
| Italiano | `www.rigsizelive.com/it` |

## Workflow voor content updates

1. Edit een taal in `translations/[lang].json`
2. Run `python3 build.py`
3. Commit + push - Vercel deployt automatisch

```bash
cd ~/rigsizelive-marketing
python3 build.py
git add .
git commit -m "update: tekst aanpassingen"
git push
```

## Eerste deploy naar Vercel

1. Maak een nieuwe GitHub repo `rigsizelive-marketing`
2. Push deze map ernaartoe
3. In Vercel: New Project -> Import Git Repository -> selecteer `rigsizelive-marketing`
4. Framework Preset: **Other** (geen build command nodig)
5. Output Directory: `.` (root)
6. Deploy
7. In Vercel project settings -> Domains: voeg `www.rigsizelive.com` toe
8. DNS: zet de CNAME record voor `www` naar `cname.vercel-dns.com`
9. Verwijder de huidige redirect van `www -> app.rigsizelive.com`

## Lokaal testen

```bash
cd ~/rigsizelive-marketing
python3 build.py
python3 -m http.server 8000
# open http://localhost:8000 (NL)
# open http://localhost:8000/en (EN)
```

## Aanpassingen aan layout/structuur

Edit `template.html` (heeft `{{KEY}}` placeholders).
Run `python3 build.py` opnieuw om alle 6 talen te regenereren.

## Talen toevoegen

1. Voeg `translations/[code].json` toe (kopie van `nl.json`, vertaal de waarden)
2. Voeg de taal-code toe aan `LANGUAGES` in `build.py`
3. Voeg toe aan de language switcher in `template.html`
4. Run `python3 build.py`

## Privacy & Voorwaarden

Privacy en Terms staan op `app.rigsizelive.com/privacy.html` en `/terms.html`.
De marketing-site linkt daarheen - geen duplicaten.

## App Store / Google Play knoppen

Tot de native apps live zijn op de stores:
- "SOON" badge op beide knoppen
- Niet-klikbaar (cursor: not-allowed)
- Browser-knop blijft actief naar `app.rigsizelive.com`

Wanneer de native apps live gaan: edit `template.html` -> verwijder `data-soon="1"` van de twee knoppen en vul de echte URLs in.
