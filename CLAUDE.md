# RigSize Live marketing site

Communiceer in het Nederlands. Dit repo staat los van de RSL-app
(`~/RigSize-Live`); verwar de twee niet.

Live: `www.rigsizelive.com` via Vercel, branch `main`.

## Bron versus output

```
template.html            <- bewerken
translations/nl.json     <- bewerken
translations/en.json  de.json  fr.json  es.json  it.json
build.py                 <- genereert alles hieronder
index.html               <- GEGENEREERD (nl), niet handmatig bewerken
de/ en/ fr/ es/ it/      <- GEGENEREERD, niet handmatig bewerken
```

## De build-stap is verplicht

`template.html` patchen zonder daarna te builden betekent dat de live site
niets ververst. De gegenereerde HTML's zijn wat Vercel serveert. Vergeten te
builden is de meest voorkomende oorzaak van "ik zie mijn wijziging niet",
ondanks een geslaagde commit en push.

Volledige workflow:

1. `template.html` en/of `translations/*.json` patchen
2. `python3 build.py`
3. Fabian commit **alle** gewijzigde bestanden via GitHub Desktop: de template
   en de zes gegenereerde HTML's
4. Push naar `main`, Vercel deployt automatisch

Voer zelf geen `git commit` of `git push` uit.

## Hardcoded versus vertaald

Niet alles loopt via `{{KEY}}` placeholders. Sommige waardes staan hardcoded in
de template. Controleer altijd eerst welke van de twee het is:

- placeholder -> aanpassen in alle zes `translations/*.json`
- hardcoded -> alleen in `template.html`

## Diagnose "ik zie geen wijzigingen"

```bash
grep -rln "OUDE_TEKST" . --include="*.html" 2>/dev/null | grep -v backup
```

- hits in `template.html`: het patchen zelf is niet goed gegaan
- hits in de per-taal HTML's (`de/index.html`): `build.py` is niet gedraaid
- geen hits lokaal: live controleren met
  `curl -s https://www.rigsizelive.com/ | grep -c "OUDE_TEKST"`
  (0 betekent live goed, dus browser-cache; 1 of meer betekent dat Vercel nog
  de oude versie serveert)

Cloudflare Web Analytics token staat in de template en moet blijven staan.
