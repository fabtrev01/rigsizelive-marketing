# RSL — projectstatus social marketing

Bijgewerkt: **12 oktober 2026**.

Werkafspraak 6 oktober: bij Meta-advertentiewerk eerst MCP proberen. Als een verwachte functie of koppeling niet werkt, Fabian vragen de koppeling te controleren voordat op Chrome wordt teruggevallen. Vaste instructie opgenomen in `AGENTS.md`.

## Huidig doel

Advertenties, posts en Reels maken voor de Facebook-pagina RigSize Live en Instagram **@rigsizelive**. De relevante productcontext staat in `AGENTS.md`. De Nederlandse en Engelse Europese verkeerscampagnes zijn gepubliceerd en ingeschakeld, elk met €3 gemiddeld/dag voor Facebook en Instagram samen. Fabian kiest voor bereik op gangbare telefoons; installatiemeting mag later. Op 6 oktober zijn de drie Europese advertenties bijgewerkt met de nieuwe EU-kaartvideo’s en Paradise Found; Meta verwerkt/beoordeelt de updates nog. De eerdere installatiecampagnes blijven uit. Native meetintegratie is uitgesteld.

## Product en gewenste boodschap

**RigSize Live** helpt windsurfers, kiters en wingers elkaar te informeren door hun actuele sessie, spot en materiaal te delen. Deelnemers kunnen vóór vertrek zien welke rigmaten anderen gebruiken. Daarnaast combineert RSL sessietracking met wind, spot en gear voor statistieken en persoonlijke analyses.

Fabians prioriteiten:

1. Samen informatie delen en elkaar helpen.
2. Helemaal gratis, zonder verrassingen of paywall.
3. Meer deelnemers maken RSL leuker en de gedeelde informatie nuttiger.
4. Het praatje aan het water blijft; de informatie is ook thuis al beschikbaar.
5. De uitgebreide tracker en de combinatie van tracking, wind en gekozen gear laten zien.

**Positionering:** RSL is uniek door het samenspel van community, live rigdelen, volledig gratis gebruik zonder paywall en uitgebreide tracking gekoppeld aan wind, spot en gear. Dit is de gewenste boodschap; een claim dat andere apps deze eigenschappen niet hebben hoort er niet bij.

**Hoofdslogan:** “Het praatje aan de kant blijft, maar jij weet thuis al of het waait.”

**Aanvullende merkzin:** “Share rigsizes, good surfkarma.”

**Vaste overkoepelende merkboodschap:** “De meest complete app voor windsurf, kite en wing”. Expliciet gekozen door Fabian voor de socials. Ondersteun deze headline met concrete voorbeelden van de combinatie van community, live rigdelen, wind- en spotinformatie, tracking en gearinzichten, helemaal gratis zonder paywall.

## Productinformatie uit de marketingmap

| Onderdeel | Relevante inhoud voor socials |
| --- | --- |
| Live rigdelen | Actieve sessie starten, materiaal invullen en op de spot delen; geen horloge nodig |
| Tracking en import | Garmin Connect en Apple Health; gebruik van een eigen horloge/tracking-app |
| Sessiedata | GPS-route, snelheid, afstand, hartslag en Alpha 500 waar beschikbaar |
| Analyses | Logboek, records, seizoenspatronen en vergelijking van materiaalcombinaties |
| Wind en spot | Voorspellingen en, waar aanwezig, windstationmetingen; spotinformatie |
| Community | Spot-chat, groepsplanning, leaderboards, events en challenges |
| Aanvullend | Wind alerts, vin-/foilcalculator en safety check-in |

Dit is een samenvatting van lokale marketingbronnen, geen volledige controle van de actuele app. Community en tracking zijn de primaire contentlijnen; de overige functies zijn ondersteunend.

## Visuele basis en bestemmingen

- Kleuren uit `template.html`: aqua `#1a9cc4`, teal `#2bb3a6`, diepblauw `#1d6ea8`, donker `#0b1220`; oranje accent `#ff7a3d`.
- Typografie website: Space Grotesk voor koppen, Inter voor lopende tekst, JetBrains Mono voor data-accenten.
- Logo's: `icons/logo-color-lg.png`, `icons/logo-white.png`, `icons/logo-192.png`.
- Appbeelden: `images/live-rigsizes.png`, `images/session-details.png`, `images/community-phone.png`, `images/phone-feed.png`, `images/spot-info.png`, windbeelden in `images/`.
- Sportbeelden: `images/hero-photo.png`, `images/windsurfer.png`, `images/kiter.png`, `images/winger.png`.

Links aangetroffen in de lokale bron; controleer werking en actuele beschikbaarheid vóór een campagne:

- Website: https://www.rigsizelive.com
- Webapp: https://app.rigsizelive.com
- Store-doorverwijzing: https://www.rigsizelive.com/app/
- App Store: https://apps.apple.com/nl/app/rigsize-live/id6771266857
- Google Play: https://play.google.com/store/apps/details?id=com.rigsizelive.app

## Meta-koppeling — gecontroleerd op 2 oktober 2026

| Asset | Naam / ID |
| --- | --- |
| Business portfolio | rigsizelive — `1003119042328703` |
| App | `988782677571964` (interface toont soms het ID als naam) |
| Systeemgebruiker | Rslcodex — Employee; beheer-ID `61594663425016` |
| App-scoped systeemgebruiker-ID | `122105936601488780`, teruggegeven door `/me` |
| Advertentieaccount | RigSize Live Ad account — `1701929497896944` |
| Facebook-pagina | RigSize Live — `1152931377906771` |
| Instagram | @rigsizelive — `17841422351517376` |

De dubbele app `1805473284128239` is niet in gebruik voor deze koppeling; laat deze ongemoeid. Andere accounts, waaronder Wildernis en het persoonlijke advertentieaccount, vallen buiten scope.

Bevestigde resultaten:

- Token is geldig, type `SYSTEM_USER`, voor de juiste app en Rslcodex.
- `expires_at = 0` en `data_access_expires_at = 0`: geen ingestelde vervaldatum. Het token kan alsnog ongeldig worden bij intrekking of gewijzigde rechten.
- Officiële endpoint `https://mcp.facebook.com/ads` werkt met het systeemgebruiker-token.
- `ads_get_ad_accounts` bevestigt RigSize als actief, bevraagbaar en ingeschakeld voor Ads MCP.
- Facebook-pagina bereikbaar; taken `ANALYZE`, `ADVERTISE`, `CREATE_CONTENT` bevestigd.
- Instagram-ID en gebruikersnaam bevestigd; endpoint voor publicatielimiet bereikbaar.
- Rechten voor advertenties, Facebook-posts en Instagram-publicatie zijn toegekend.
- **Nog niet end-to-end getest:** daadwerkelijke Facebook-/Instagram-publicatie. Er is geen testpost geplaatst. De route voor organische publicatie moet bij de eerste opdracht worden ingericht en getest binnen die opdracht.

Kernrechten: `ads_mcp_management`, `ads_management`, `ads_read`, `pages_show_list`, `pages_read_engagement`, `pages_manage_posts`, `instagram_basic`, `instagram_content_publish`, `instagram_manage_insights`, `read_insights`. Fabian heeft bewust extra rechten laten staan; dit verruimt de opdrachten niet automatisch.

### Lokale techniek

- Tokenbestand: `~/.codex/meta-ads-rigsize/access-token` (geheim; inhoud nooit weergeven).
- Veilig opslaan/vervangen: `~/.codex/meta-ads-rigsize/save-token.command` via verborgen invoer.
- Headerhelper: `~/.codex/meta-ads-rigsize/headers.py`; voer deze niet uit met zichtbare uitvoer, want die bevat het token.
- MCP-servernaam in Codex-configuratie: `meta-ads-rigsize`.
- Deze sessie testte de verbinding rechtstreeks via HTTP. Neem niet aan dat native Meta-tools in iedere nieuwe chat automatisch beschikbaar zijn.
- Bestaande Meta MCP-conversatie-ID voor voortzetting van deze chat: `R7xk2MvQ9bL4sT8wC3nA`. Gebruik bij tools die het veld accepteren. Maak voor een afzonderlijke nieuwe conversatie een eigen ID.

## Contentaanpak voor de volgende opdrachten

### Nederlandse videosnippets — voorbereiding 2 oktober 2026

Fabian vraagt om Meta-advertentieconcepten met de drie Nederlandse snippets, met app-installaties als gewenst resultaat. Advies: drie losse videoadvertenties binnen dezelfde advertentieset, zodat iedere boodschap afzonderlijk zichtbaar is in de resultaten (geen gegarandeerd gelijk verdeelde A/B-test).

- Bron: `/Users/fabiantrevisan/rsl-video/out/`; bijbehorende brief en Nederlandse copy gelezen en representatieve frames van alle drie bekeken. Vormgeving is nagebouwde app-UI met demo-data, geen echte sessies. H.264, 1080×1920, zonder audiotrack.
- `rsl-waait-het-nl.mp4`: 14,37 s; video-ID `1800578284312872`.
- `rsl-je-sessie-nl.mp4`: 12,67 s; video-ID `1123926873495423`.
- `rsl-gratis-nl.mp4`: 11,60 s; video-ID `941571308571264`.
- Alle drie geüpload naar de advertentiebibliotheek van RigSize en verwerking bevestigd als `ready`. Inmiddels gebruikt in zes gepauzeerde advertenties (zie actuele campagnestatus onderaan).
- Nederlandse teksten en uploadgegevens staan in `campaigns/rsl-snippets-nl/concept.json`. Hergebruik deze uploads bij voortzetting.
- Vorige advertentie `Carrousel NED aug 2026` (`120251892308230100`) gebruikt `https://www.rigsizelive.com/app`. De campagne is `OUTCOME_TRAFFIC`, advertentieset optimaliseert op `LANDING_PAGE_VIEWS`, regio NL, €3/dag. Deze instellingen zijn alleen gelezen, niet aangepast of als keuze voor de nieuwe campagne aangenomen.
- Downloadpagina live gecontroleerd: Apple-app `6771266857`, Android `com.rigsizelive.app`. De storelinks bevatten nog de attributielabels `meta-carrousel-ned` / `carrousel-ned`; daardoor zijn downloads van nieuwe snippets via deze pagina niet afzonderlijk herkenbaar aan die labels.
- Mobiele app-koppeling voltooid: iOS bundle-ID `com.rigsizelive.app`, iPhone Store-ID `6771266857`; Android Google Play package `com.rigsizelive.app`, class `com.rigsizelive.app.MainActivity`. Opgeslagen in Meta App settings > Basic. Graph `advertisable_applications` bevestigt nu zowel `itunes` als `google_play` bij app `988782677571964` in het juiste advertentieaccount.
- Fabian koos expliciet eerst de mobiele app-koppeling voor app-installaties. Die storekoppeling is nu afgerond. Regio Nederland en €3 gemiddeld per dag samen zijn inmiddels bevestigd. Niets activeren.
- Installatiemeting nog niet ingericht/getest: in de bekeken native iOS/Android-configuratie in `/Users/fabiantrevisan/RigSize-Live` geen Facebook App-ID/ClientToken/App Events-configuratie gevonden. iOS bevat FBSDK via de social-loginplugin; aanwezigheid van de dependency bewijst geen werkende installatiemeting. Appbron niet gewijzigd. Vervolg: native eventintegratie onderzoeken, implementeren, op toestel controleren in Meta en zo nodig nieuwe storebuilds uitbrengen. Android verwijdert momenteel expliciet AD_ID-permissie; dit niet ongemerkt wijzigen.
- Bewijs van opgeslagen Android-platform: `campaigns/rsl-snippets-nl/meta-app-koppeling.jpg`. iOS ook na herladen bevestigd; beide stores via API bevestigd.

Start met drie concepten (nog niet geproduceerd of goedgekeurd):

1. **Community-Reel:** thuis twijfelen over de wind, gedeelde rigmaten bekijken, aan de kant samen optuigen. Afsluiten met de hoofdslogan en “Deel jouw rig”.
2. **Gratis-post/carrousel:** wat je samen deelt, wat je eraan hebt, helemaal gratis zonder paywall. CTA: “Doe mee op jouw spot”.
3. **Tracker-demo:** echte sessie tonen met route, wind en geselecteerde gear; één duidelijk inzicht uitlichten. CTA: “Haal meer uit je sessie”.

Voor een concrete campagne nog te bepalen: organisch of betaald, doelgroep/discipline, regio en taal, doel, budget en looptijd indien betaald, materiaal en bestemming. Vraag alleen wat de betreffende opdracht nodig heeft.

## Openstaande controles en bronverschillen

- Fabian heeft de claim “geen andere app heeft dit” laten vallen. De unieke combinatie van eigenschappen blijft de positionering; verificatie van exclusiviteit is geen openstaand actiepunt.
- README meldt nog dat native apps binnenkort verschijnen. De actuele lokale template bevat storelinks en de Nederlandse tekst meldt beschikbaarheid. De oudere README is hiervoor geen betrouwbare actuele bron.
- Template bevat voorbeeldsessies, snelheden, online-aantallen en testimonials met portret-placeholders. Niet als echte gebruikersbewijzen hergebruiken zonder verificatie.
- Claims over aantallen spots, updatefrequenties en actuele functies controleren wanneer een uiting daarop leunt.
- Live informatie hangt af van gedeelde actieve sessies; afwezigheid van sessies is geen bewijs van windstilte.

## Geraadpleegde bronnen

- `translations/nl.json`: productuitleg, community, tracking, gratis gebruik en functies.
- `template.html`: visuele stijl, assets, storelinks, voorbeelddata en testimonials.
- `translations/calculator-nl.json`: achtergrond calculator.
- `app/index.html`: store-doorverwijspagina.
- `README.md` en `CLAUDE.md`: repositorystructuur en websiteworkflow.
- Fabians instructies en screenshots in deze chat, plus de alleen-lezen Meta API-controles van 2 oktober 2026.

Bij volgende werkzaamheden: noteer gemaakte contentbestanden, goedgekeurde versies, publicatie-ID's/links, eventuele campagne-ID's en nog openstaande punten. Sla geen geheimen op.

## Nieuwe campagne — actuele status 2 oktober 2026

- Meta-app `988782677571964` naar **Live** gezet na expliciete toestemming van Fabian. Privacy policy en verwijderinstructies: `https://www.rigsizelive.com/privacy-en`; voorwaarden: `https://www.rigsizelive.com/terms-en`; categorie Lifestyle. Geen appnaam of permissies aangepast.
- Campagne `120252356146190100`, **RSL | App-installaties | NL | Videosnippets**: OUTCOME_APP_PROMOTION, status en effective_status PAUSED, gedeeld dagbudget **300 eurocent**. Geen apart budget per advertentieset. UI bevestigt €3 gemiddeld per dag, maximaal €5,25 op losse dagen en €21/week.
- Android-set `120252360193840100`; iOS-set `120252360247570100`. Beide PAUSED, APP_INSTALLS, mobiel, alleen Nederland, Facebook + Instagram.
- Zes advertenties aangemaakt, elk status PAUSED. Bij eindcontrole effective_status PENDING_REVIEW: Meta-beoordeling nog niet voltooid, geen levering vanuit deze campagne.

| Snippet | Android-ad | iOS-ad |
| --- | --- | --- |
| Waait het? | 120252360239380100 | 120252360252680100 |
| Je sessie | 120252360239980100 | 120252360252950100 |
| Gratis. Echt. | 120252360240320100 | 120252360256310100 |

### Opgeloste blokkades en resterend werk

- Android-storevalidatie slaagde met expliciet `&gl=NL` in de Google Play-link. Meta normaliseert de opgeslagen promoted_object-URL vervolgens; de creative behoudt de Nederlandse link.
- Creative-fout 1885183 verdween na de geautoriseerde Live-overgang. Ook iOS-storevalidatie 2446333 slaagde daarna. Beide platformen accepteren nu de drie video-creatives.
- **Nog niet gereed voor activering op moderne iPhones:** de eindcontrole toont dat Meta de gevraagde iOS-targeting heeft genormaliseerd naar `iOS_ver_2.0_to_14.4`. Niet als volledige iOS-dekking presenteren. Moderne iOS-campagne-inrichting/attributie moet worden opgelost, met behoud van het totale budget. De huidige campagne-interface toont geen iOS 14+-optie onder extra campagnedetails.
- Installatiemeting blijft niet ingericht/end-to-end geverifieerd; zie native configuratiebevindingen hierboven. Geen appcode gewijzigd, geen storebuild gemaakt.
- Er blijft één uitgeschakeld diagnostisch UI-concept over: set `120252360144630100`, naam `RSL | iOS | CONCEPT - storevalidatie nodig`, placeholder-ad `120252360144640100`. Niet publiceren. Daardoor toont de UI 3 sets/7 ads; de bedoelde campagne bevat **2 echte sets/6 video-ads**. Discard werd geannuleerd omdat Meta dat als onomkeerbaar aanmerkt; geen toestemming voor permanente verwijdering gevraagd of verkregen.
- Bestaande campagnes niet aangepast. Geen nieuwe advertenties geactiveerd.

Campagnelink: https://www.facebook.com/adsmanager/manage/campaigns/edit?act=1701929497896944&selected_campaign_ids=120252356146190100

Bestanden: `campaigns/rsl-snippets-nl/concept.json` (copy/IDs), `verification.json` (API-eindcontrole), `meta-campagne-gepauzeerd.jpg` (UI-bewijs). Geen tokens opgeslagen.

### Vervolg moderne iOS — 2 oktober 2026

- Diagnose bevestigd: de bestaande campagne heeft `is_skadnetwork_attribution=false`. Wijzigen wordt geweigerd met 2446698 (campagnetype niet meer wijzigbaar).
- Nieuwe iOS 14+-campagne `120252360351140100` aangemaakt PAUSED, vlag true. Bestaande campagnebudget verlaagd naar €1,50; nieuwe campagne €1,50. Beide teruggelezen PAUSED, totaal **€3 gemiddeld/dag**. Dit vervangt het hierboven genoemde enkele campagnebudget van €3.
- Moderne iOS-set validatie wordt geblokkeerd door **2446981 SKAdNetwork Not Ready**. Geen nieuwe iOS-set of dubbele ads gemaakt. Events Manager toont geen databronnen voor het gekozen RSL-account.
- Structurele oplossing en alternatief vastgelegd in `campaigns/rsl-snippets-nl/IOS-INSTALLATIEMETING.md`. Native appbron nog niet aangepast. Apprepo CLAUDE.md vereist voorstel/akkoord voordat code wordt gewijzigd; keuze voor native meetintegratie versus verkeerscampagne nog te bevestigen.
- Oude iOS-set blijft PAUSED en is geen oplossing voor moderne toestellen. Niet activeren.

### Definitieve richting: verkeerscampagne voor alle telefoons

- Fabian: “Ik wil gewoon goede advertenties draaien nu voor alle gangbare telefoons en als de meting niet optimaal is nu maakt mij dat niet uit. Dat kan later altijd nog eens.” Geen native wijzigingen nodig voor deze route; SKAdNetwork is geen blocker voor dit verkeersconcept.
- Vervangende campagne `120252360444710100`, **RSL | NL | Videosnippets | Downloads**, OUTCOME_TRAFFIC, CBO €3 gemiddeld/dag, PAUSED.
- Set `120252360444950100`: WEBSITE / LANDING_PAGE_VIEWS, alleen NL, mobiel, Facebook/Instagram, geen user_os/device-modelbeperking. Eén set voor Android en iPhone samen.
- Ads PAUSED: Waait het? `120252360446160100`; Je sessie `120252360456410100`; Gratis. Echt. `120252360460650100`. Meta-verwerking/beoordeling nog lopend bij teruglezen. Download-CTA, bestaande drie video's, Nederlandse copy.
- Bestemming `https://www.rigsizelive.com/app/` met snippet-UTMs. Live gecontroleerd: HTTP 308 naar `/app`, daarna HTTP 200; client-side iPhone/iPad- en Android-storekeuze aanwezig. Storelinks bevatten nog de oude carrousel-attributielabels; geen betrouwbare nieuwe installatietoewijzing claimen. Website niet gewijzigd/gepubliceerd.
- Advertentievoorbeeld in Ads Manager bevestigd voor RigSize Live en @rigsizelive. Alle automatische creative enhancements staan uit.
- Eerdere installatiecampagnes `120252356146190100` en `120252360351140100` zijn PAUSED bevestigd. Hun budgetten zijn geen extra uitgaven zolang ze uit blijven; alleen het nieuwe verkeersconcept van €3 is bedoeld voor lancering. Geen bestaande lopende campagne aangepast.
- Bestanden: `traffic.json`, `traffic-verification.json`, `meta-traffic-preview.jpg` in `campaigns/rsl-snippets-nl/`.
- Link: https://www.facebook.com/adsmanager/manage/campaigns/edit?act=1701929497896944&selected_campaign_ids=120252360444710100
- Nog niet geactiveerd; oorspronkelijke opdracht was concept. Installatiemeting hoeft niet eerst opgelost te worden om deze verkeerscampagne te gebruiken.

### Locatiefout hersteld in Ads Manager — 2 oktober 2026

- Rode fout #1870194 betrof een verouderd locatietargetingtype in het openstaande concept van set `120252360444950100`.
- Graph-update naar `home` + `recent` geaccepteerd; Meta las vervolgens `frequently_in`, `home`, `recent` terug. Geen status of budget aangepast. Het toenmalige UI-concept bleef aanvankelijk de fout tonen.
- Fabian gaf akkoord voor verwerpen van dat concept. Bij hervatten was de bevestigingsdialoog al verdwenen, waren interesse/einddatum afwezig en toonde de opnieuw geopende set geen rode fout meer. Niet door de agent bevestigd wie het concept heeft verworpen.
- Opnieuw als concept ingesteld: einddatum **1 november 2026 00:00**, zoals de UI die toont (GMT+2), en **Windsurfing (water sport)** als Advantage+ doelgroepsuggestie. Nederland bleef als enige locatie geselecteerd. Budget €3 gemiddeld/dag en Facebook/Instagram mobiel behouden.
- Eindcontrole UI: **All edits saved**, Windsurfing en einddatum aanwezig, geen #1870194 of “Review 1 error”. Niet op Publish geklikt; set staat Off. Nieuwe conceptwijzigingen zijn nog niet gepubliceerd/geactiveerd.
- Bewijs: `campaigns/rsl-snippets-nl/meta-locatiefout-hersteld.jpg`. Gele plaatsingsaanbeveling blijft zichtbaar; geen rode blokkade meer in dit scherm.

### Engels Europees concept — 2 oktober 2026, nog onvolledig

- Op verzoek aparte kopie aangemaakt via Ads Manager: `120252363387660100`, **RSL | EN | Europe | Videosnippets | Downloads**, concept, campagneschakelaar UIT, €3 gemiddeld/dag totaal voor deze campagne.
- Set `120252363387650100`, **RSL | EN | 8 regions | All phones | FB + IG**, UIT: NL, BE, FR, DE, ES, IT, NO en uitsluitend Engeland (GB-regio 4079). Locaties zichtbaar gecontroleerd. Windsurfing als Advantage+ suggestie, mobiel FB/IG, WEBSITE/LANDING_PAGE_VIEWS, einddatum 1 november 00:00 behouden.
- Drie ads UIT met Engelse namen, primary text, headlines en EN-campagne-UTMs opgeslagen: Free. Really. `120252363387630100`; Your session `120252363387640100`; Is it blowing? `120252363387670100`.
- **Nog NIET klaar:** Engelse video's moeten nog worden toegevoegd. In Free. Really. is de Nederlandse video verwijderd (nu geen media). De twee andere ads bevatten voorlopig de Nederlandse bronvideo. Niet publiceren voordat alle drie vervangen en gecontroleerd zijn. Controleer ook automatische video-effecten: duplicatie toonde Add video effects standaard aan.
- API gaf eerst leesresultaten, daarna alle gecontroleerde Graph-verzoeken `API access blocked` OAuthException code 200; Ads MCP gaf HTTP 401. Oorzaak niet vastgesteld. Geen token gewijzigd. Nieuwe video-uploads via API niet geslaagd.
- Browserupload geblokkeerd: ChatGPT Chrome-extensie mist **Allow access to file URLs**. Gebruiker gevraagd dit aan te zetten; geen toestemming veronderstellen. Filechooser.setFiles faalde, geen Engelse video toegevoegd.
- Browser-tab 963131752 gemarkeerd voor vervolg. Bestanden: `campaigns/rsl-snippets-en/concept.json`, `meta-concept-pending-video.jpg`.
- Nederlandse broncampagne was bij aanvang van dit werk **Preparing / aan**, Nederlandse set ACTIVE en einddatum/interesse reeds gepubliceerd. Dit is door de gebruiker of buiten deze actie veranderd; agent heeft de Nederlandse campagne niet geactiveerd en nu niet gewijzigd. Bestaande ENG-carrouselcampagne stond ook Active.

### Engelse video’s toegevoegd — 2 oktober 2026

- Na gebruikersbevestiging van de Chrome-extensie-instelling is browserupload van alle drie EN-MP4’s geslaagd. Geen API-token gewijzigd.
- Alle drie advertenties gebruiken nu het juiste Engelse bestand; via **Edit media → Edit video** is voor elk bestand **Editing 16 placements** bevestigd: `rsl-gratis-en.mp4` (0:12), `rsl-je-sessie-en.mp4` (0:13), `rsl-waait-het-en.mp4` (0:14), allemaal 1080×1920. Engelse copy en download-CTA behouden; EN-UTM-bestemmingen teruggelezen.
- Automatische video touch-ups, text improvements, layout details, relevant comments, CTA enhancements en video effects uitgeschakeld. Onbedoelde Related media bij Gratis en Waait verwijderd uit het concept; nul geselecteerde extra media bevestigd.
- **Resterende publicatieblokkade:** Meta toont op de drie aangepaste advertenties fout **#2446880: WhatsApp number required**. Bestemming is Website en Browser add-ons staat op None. Bij Waait is Messaging apps tijdelijk bekeken (WhatsApp niet gekoppeld/niet aangevinkt), daarna teruggezet naar None; Download-CTA opnieuw ingesteld. Ook na herladen blijft fout bestaan. Oorzaak niet vastgesteld; geen WhatsApp-account gekoppeld en niets gepubliceerd.
- Campagne blijft concept/UIT met €3 gemiddeld per dag, acht eerder gecontroleerde regio’s en einddatum behouden. De inhoud is voorbereid, maar niet als publicatiegereed presenteren zolang validatiefout bestaat. Nederlandse campagne niet aangepast.
- Bewijs: `campaigns/rsl-snippets-en/meta-english-videos-validation.jpg`. Browser-tab 963131752 op Chrome-verbinding 4 gemarkeerd voor vervolg.

### Engelse Instagram-Reel met muziek — 3 oktober 2026

- Volledige Engelse video en caption door Fabian goedgekeurd; Instagram-composer voorbereid voor uitsluitend @rigsizelive, nog niet gepubliceerd. Publicatie aangehouden voor muziekkeuze.
- Fabian leverde na zoeken in Meta Sound Collection `/Users/fabiantrevisan/Downloads/Paradise Found.mp4` aan en vroeg deze toe te voegen. Bestand bevat alleen AAC-audio (2:25), metadata-ID `972359113839394`.
- Voorbeeld gemaakt: `/Users/fabiantrevisan/rsl-video/out/rsl-master-en-paradise-found.mp4`. Eerste 34,63 seconden van muziek gebruikt, fade-in 0,5 seconde en fade-out 1,5 seconde; volume genormaliseerd. Originele H.264-videostream zonder hercodering behouden, 1080×1920/30 fps. AAC-stereo toegevoegd en decodeercontrole geslaagd (circa -14,84 LUFS, piek -1,26 dBTP).
- Nieuwe versie eerst ter beoordeling aangeboden; nog niet geüpload of gepubliceerd met muziek.
- Fabian meldde eerder dat de advertenties live zijn; dit is een gebruikersmelding, geen nieuwe onafhankelijke controle van alle campagnestatussen.

### Instagram-Reel gepubliceerd — 3 oktober 2026, 11:52

- Na goedkeuring van muziekvoorbeeld de volledige Engelse video met Paradise Found gepubliceerd op uitsluitend Instagram @rigsizelive, openbaar, met de goedgekeurde caption. Geen Facebook-crosspost of boost.
- Bestand: `/Users/fabiantrevisan/rsl-video/out/rsl-master-en-paradise-found.mp4` (34,63 s). Meta meldde vóór publicatie geen copyrightproblemen.
- Publicatie bevestigd in Meta Business Suite: **Reel · Published on: Sat Oct 3, 11:52am**.
- Content-ID: `17911121121552395`.
- Permalink: https://www.instagram.com/reel/DeBx7c1AtFL/
- Bewijs: `reel-published-2026-10-03.jpg`.

### Muziek in alle NL- en EN-snippetadvertenties — 3 oktober 2026

- Op expliciet verzoek van Fabian Paradise Found (Brian Withycombe, aangeleverd uit Meta Sound Collection) toegevoegd aan alle zes bestaande live snippetadvertenties en de creatieve wijzigingen gepubliceerd via Ads Manager.
- Zes bestanden in `/Users/fabiantrevisan/rsl-video/out/`: `rsl-{gratis,je-sessie,waait-het}-{nl,en}-paradise-found.mp4`. Originele videostream behouden (1080×1920, 30 fps); AAC-stereo toegevoegd, genormaliseerd met doel -16 LUFS, fade-in 0,3 s en fade-out 1 s. Lengtes 11,60 / 12,67 / 14,37 s; volledige audio/video-decodecontrole voor alle zes geslaagd. Originele stille bestanden behouden.
- NL-campagne `120252360444710100`: Je sessie `120252360456410100`, Gratis `120252360460650100`, Waait `120252360446160100` bijgewerkt.
- EN-campagne `120252363387660100`: Free `120252363387630100`, Your session `120252363387640100`, Is it blowing `120252363387670100` bijgewerkt.
- Voor elke advertentie via Edit media → Edit video het juiste `paradise-found.mp4`-bestand bij **Editing 16 placements** gecontroleerd. Original crop en volledige videolengte behouden. Geen AI-beelden geselecteerd; automatische video/text/layout/CTA/effectverbeteringen bleven uit.
- Iedere advertentie afzonderlijk gepubliceerd. Meta bevestigde updates en toonde Processing/In review. Alle zes advertenties bleven ingeschakeld; beide campagnes waren bij aanvang Active. Dit vervangt eerdere notities dat de Engelse campagne nog concept/UIT was. Geen nieuwe campagnes of advertenties gemaakt.
- Copy, CTA, bestemmingen, doelgroep, planning en budgetten niet gewijzigd. Beide campagnes behouden hun bestaande budget van €3 gemiddeld per dag per campagne.
- Twee reeds bestaande, niet-gerelateerde accountconcepten ongemoeid gelaten; geen globale Review and publish uitgevoerd.
- Bewijs: `ads-music-nl-2026-10-03.jpg`, `ads-music-en-2026-10-03.jpg`. Nieuwe creaties zijn ingediend; definitieve Meta-goedkeuring nog niet bevestigd.
- Fabian bevestigde eerder dat hij de Engelse Reel zelf ook in zijn Story heeft gedeeld. Hoogtepunt niet onafhankelijk gecontroleerd.

### Europese advertenties met EU-kaart en muziek — 6 oktober 2026

- Fabian vroeg de nieuwe bestanden met `eu` in de naam te gebruiken in de Europese advertenties, met dezelfde muziek. Hij verduidelijkte expliciet: alleen vervangen in de Europese advertenties; geen lokale bestanden verwijderen.
- Drie exports gemaakt in `/Users/fabiantrevisan/rsl-video/out/`: `rsl-gratis-en-eu-paradise-found.mp4`, `rsl-je-sessie-en-eu-paradise-found.mp4`, `rsl-waait-het-en-eu-paradise-found.mp4`. De stille EU-bronnen en oude bestanden blijven behouden. Het volledige EU-masterfilmpje is niet gebruikt; deze campagne bevat snippets.
- Paradise Found van Brian Withycombe toegevoegd zoals eerder: originele videostream behouden, AAC-stereo 192k/48k, normalisatiedoel -16 LUFS, 0,3 s fade-in en 1 s fade-out. Duur 11,60 / 12,67 / 14,37 s. Volledige audio/video-decodecontrole geslaagd; frames met Europese kaart en sessie-inzicht visueel gecontroleerd.
- Bestaande Europese campagne `120252363387660100`, advertentieset `120252363387650100`: Free. Really. `120252363387630100`, Your session `120252363387640100`, Is it blowing? `120252363387670100` afzonderlijk bijgewerkt en gepubliceerd via Ads Manager.
- Voor elk van de drie advertenties juiste EU+muziek-bestand bevestigd bij **Editing 16 placements**. Volledige lengte en Original crop behouden. Geen AI-afbeeldingen toegevoegd; bestaande tekst, CTA, bestemmingen, budget, doelgroep, planning en ingeschakelde status behouden.
- Meta stelde bij Free. Really. en Your session oude video’s voor als Related media. Deze alternatieven uit de advertentie verwijderd en 0 geselecteerde media bevestigd. Bij Is it blowing? geen Related media actief in Review defaults. De mediabibliotheek zelf is niet opgeschoond.
- Meta bevestigde de publicaties. Eindstatus: Free. Really. In review; Your session en Is it blowing? Processing. Definitieve goedkeuring nog niet bevestigd. Alle drie aan; geen nieuwe advertenties aangemaakt. NL-campagne en twee bestaande accountconcepten ongemoeid gelaten.
- Bewijs: `/Users/fabiantrevisan/rsl-video/out/eu-ads-published-2026-10-06.jpg`.

### Verzoek prestatieanalyse — 12 oktober 2026

- Fabian meldt weinig nieuwe RSL-gebruikers en vraagt de huidige campagnes te analyseren.
- Beschikbare tools gecontroleerd en pluginzoekfunctie geraadpleegd: de eerder gebruikte MCP-server `meta-ads-rigsize` is in deze sessie niet als aanroepbare Meta Ads-tools beschikbaar. Geen actuele campagnecijfers opgehaald; geen nieuwe authenticatiefout of verlopen token vastgesteld.
- Conform afspraak eerst Fabian vragen de bestaande koppeling te controleren; niet stilzwijgend via Chrome of een andere API doorgaan. Geen advertenties of budgetten gewijzigd.
- Na herstel: NL en EN vergelijken over dezelfde volledige dagen (bij voorkeur 5–11 oktober), per advertentie/land/platform; uitgaven, bereik, frequentie, uitgaande klikken, landingpagebezoeken en eventuele gemeten installaties. RSL-registraties afzonderlijk vergelijken; landingpagebezoeken zijn geen bewijs van nieuwe gebruikers.

### MCP-hercontrole na herstart — 12 oktober 2026

- Fabian bevestigt herstart; screenshot toont `meta-ads-rigsize` ingeschakeld. Andere MCP-tools zijn na herstart beschikbaar, Meta-tools nog niet.
- Rechtstreekse alleen-lezen MCP-initialisatie naar `https://mcp.facebook.com/ads` met het bestaande lokaal opgeslagen token geeft HTTP 401: `Permission Error`, `API access blocked.`, code 200. Token niet weergegeven of gewijzigd. Dit bevestigt een toegangsweigering, niet specifiek een verlopen token; oorzaak nog onbekend.
- Campagneanalyse nog niet uitgevoerd. Fabian meldt 3 nieuwe RSL-gebruikers in de afgelopen zeven dagen; herkomst niet vastgesteld. Voor browseranalyse eerst afgestemde terugval vragen conform projectafspraak.

### Prestatieanalyse via Chrome — 12 oktober 2026

Fabian gaf expliciet akkoord voor browseranalyse na de MCP-toegangsweigering. Alleen rapportageweergaven gewijzigd; geen campagnes, advertenties, budgetten of publicaties aangepast. Bron: live Ads Manager, account 1701929497896944. Periode in de interface: **5–11 oktober 2026**, Amsterdam Time (URL gebruikt exclusieve eindgrens 12 oktober). Beide verkeerscampagnes en alle zes snippets Active; overige campagnes Off en €0 uitgaven in deze periode.

| Campagne | Uitgaven | Bereik | Impressies | Frequentie | Linkklikken | Link-CTR | Landingpagebezoeken | Kosten/bezoek |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EN Europa | €20,45 | 4.645 | 6.458 | 1,39 | 435 | 6,74% | 387 | €0,05 |
| NL | €21,07 | 2.139 | 2.872 | 1,34 | 225 | 7,83% | 213 | €0,10 |

Samen €41,52, 660 linkklikken en 600 landingpagebezoeken. Bereik niet optellen wegens mogelijke overlap. Fabian meldt 3 nieuwe RSL-gebruikers in de afgelopen zeven dagen; exacte cohort/datums en advertentieherkomst niet onafhankelijk bevestigd. €13,84 uitgaven per gemelde nieuwe gebruiker en verhouding 3/600 = 0,5% zijn slechts beschrijvende vergelijkingen, geen gemeten campagne-CPA of attributie/conversieratio. Linkklikken zijn geen unieke gebruikers of noodzakelijk uitsluitend uitgaande klikken; ook LPV zijn geen unieke personen/installaties. Geen app-/registratiemeting opgehaald.

- EN landenuitgaven: Spanje €17,42 (85,2%), Frankrijk €1,49, Italië €1,11, België €0,29, Verenigd Koninkrijk €0,08, Duitsland €0,03, Noorwegen €0,02, Nederland €0,01. EN kliks: Spanje 366, Frankrijk 31, Italië 31, België 6, VK 1. Dit is geen bewijs dat Spanje slechte gebruikers oplevert; registraties per land ontbreken.
- Platform: EN Facebook €20,40 / 432 kliks, Instagram €0,05 / 3 kliks. NL Facebook €21,00 / 225 kliks, Instagram €0,07 / 0 gerapporteerde kliks. Totaal 99,7% van uitgaven Facebook; Instagram onvoldoende levering om prestaties te beoordelen.
- EN advertenties: Is it blowing? €16,84 / 328 LPV; Your session €3,47 / 55 LPV; Free. Really. €0,14 / 4 LPV. NL: Waait het? €20,97 / 213 LPV; Gratis en Je sessie elk €0,05 / geen gerapporteerde LPV. Geen eerlijke A/B-test; varianten met nauwelijks uitgaven niet afkeuren op deze cijfers.
- Live downloadpagina `/app/` op desktop toont Nederlandse tekst en beide storelinks. Apple `ct=meta-carrousel-ned` en Google `utm_campaign=carrousel-ned` staan nog hardcoded, ook voor de EN-route. Dit bevestigt ongeschikte labels voor splitsing naar huidige campagne. Lokale `app/index.html` bevat OS-detectie en automatische storedoorverwijzing. Mobiele Facebook-/Instagram-in-appbrowserroute en installatie/registratie niet end-to-end getest; geen technische fout bewezen. Website niet gewijzigd.
- Advies: budget voorlopig niet verhogen; eerst mobiele doorklik/installatie/registratieroute testen en uitval per stap/land/OS zichtbaar maken. Daarna gecontroleerd scherper geografisch testen en gericht Instagram-testen binnen het afgesproken budget als Fabian dat wil. Goedkope LPV alleen bewijzen geen gebruikersgroei; app-installatieoptimalisatie blijft een afzonderlijk implementatietraject.
- Bewijs: `campaigns/analysis-2026-10-12/campagnes-week.jpg`. Rapportage-export niet bruikbaar ontvangen; bovenstaande cijfers rechtstreeks uit Ads Manager gelezen.

### Verbindingsdiagnose — 12 oktober 2026

- Op verzoek van Fabian lokale MCP-configuratie gecontroleerd: juiste endpoint en bestaande `http_headers_helper`; lokaal tokenbestand aanwezig en niet leeg. Geen geheimen weergegeven of gewijzigd.
- Nieuwe alleen-lezen test: MCP initialize opnieuw HTTP 401 `API access blocked.` (code 200). Ook Graph v26.0 `/me?fields=id` en `/me/permissions` geven OAuthException code 200 `API access blocked.`. Blokkade treft dus ook Graph API met dit token; geen uitsluitend Codex/MCP-probleem. Niet bewezen dat token verlopen is, of welke app-/businessbeperking de oorzaak is.
- Volgende stap: in Meta Developers bij app 988782677571964 waarschuwingen/vereiste acties en API-toegangsstatus controleren, plus Business Support Home voor beperkingen; op basis van exacte melding herstel kiezen. Geen token intrekken of nieuw aanmaken voordat oorzaak duidelijk is.
- Fabian heeft rotatie van NL/EN snippets goedgekeurd (4 dagen Gratis, daarna 4 dagen Je sessie, €3 gemiddeld/dag per campagne). Nog niet ingesteld: verbinding herstellen; browserwijziging nog niet apart afgestemd. Startdata pas bij daadwerkelijke uitvoering vastleggen.

### Meta-dashboard nagekeken na inloggen — 12 oktober 2026

- Juiste app 988782677571964 staat Live; dashboard en centrale Required actions tonen geen vereiste acties. App-rate-limit 0% gebruikt, 100% over; geen gebruikers throttled.
- Beide appmeldingen bekeken in Alerts: Live-modus gewijzigd op 2 oktober en welkomstbericht Marketing API van 1 oktober. Geen blokkademelding in dit overzicht.
- Business Support Home gefilterd op rigsizelive toont geen account-/assetproblemen in de afgelopen 30 dagen. Dit sluit andere of oudere beperkingen niet uit.
- Oorzaak `API access blocked` blijft onbewezen. Geen instellingen, tokens of advertenties veranderd. Mogelijke volgende diagnose: token/rechten controleren of een nieuw token testen zonder het oude in te trekken; bij dezelfde fout Meta-support met foutcode/trace-ID.

### Meta MCP hersteld na identiteitsbevestiging — 12 oktober 2026

- Fabian voltooide Meta-passkeyverificatie bij systeemgebruikers. Daarna slaagde dezelfde MCP-initialisatie met het bestaande token (HTTP 200); tools/list gaf 97 tools. Tijdelijk verband met verificatie vastgesteld, exacte interne oorzaak niet bewezen.
- `ads_get_ad_accounts` via officiële MCP bevestigt uitsluitend RSL-account 1701929497896944: ACTIVE, MCP enabled, queryable, betaalmethode aanwezig, EUR, minimum dagbudget 90 cent. Verbinding via directe MCP HTTP-route werkt weer; native tools zijn niet automatisch in deze sessie geladen.
- Business Settings > Integrations > Ads MCP server toont 7 van 7 acties toegestaan. Bestaande assettoegang van Rslcodex aanwezig. Geen nieuw token gemaakt of oude token ingetrokken; geen rechten/budgetten/advertenties gewijzigd.
- Openstaande goedgekeurde snippetrotatie nog uitvoeren via herstelde MCP; geen startdatum of schakelmoment al ingesteld.

### Tijdelijke videorotatie, fase 1 actief — 12 oktober 2026 circa 19:20

- Fabian gaf akkoord de voorgestelde rotatie uit te voeren: vier dagen Gratis/Free, daarna vier dagen Je sessie/Your session, bestaand budget behouden.
- Via officiële Meta MCP actuele campagnes (ACTIVE, elk EUR 3/dag), sets (ACTIVE, einddatum 2026-11-01T00:00:00+0100) en zes actieve ads gecontroleerd. `ads_get_ad_entities` draft-mode is niet beschikbaar voor dit account; melding gradual rollout. `ads_update_entity` werkt wel en retourneert success=true, is_draft=false: directe live statusupdates.
- Gepauzeerd en opgeslagen status bevestigd: NL Waait 120252360446160100, NL Je sessie 120252360456410100, EN Is it blowing 120252363387670100, EN Your session 120252363387640100. NL effective status PAUSED; EN effective status tijdelijk IN_PROCESS, configured status PAUSED.
- Actief gehouden en bevestigd: NL Gratis 120252360460650100 en EN Free 120252363387630100. Budgets, creatives, muziek, doelgroep en einddatum onveranderd. Geen nieuwe campagnes of advertenties.
- VOORSTEL, NOG NIET INGEPLAND: 16 oktober 19:20 Europe/Amsterdam wisselen naar Je sessie/Your session; 20 oktober 19:20 alle zes terug actief om oorspronkelijke toestand te herstellen en test af te ronden.
- Poging tot heartbeat-automation afgewezen door automatische veiligheidscontrole: financiële toekomstige statuswijzigingen en herstelactie vragen expliciete toestemming voor scheduler. Er is GEEN automation aangemaakt. Niet omzeilen met een andere scheduler/regels. Fabian expliciet vragen de automatische wissel, herstelactie en beëindiging van de automation goed te keuren. Eerste fase is al toegepast; volgende wissel is nog niet gegarandeerd/gepland.

### Automatische opvolging bevestigd — 12 oktober 2026

- Fabian gaf expliciet akkoord op automatische wissel op 16 oktober 19:20 en herstel van alle zes advertenties op 20 oktober 19:20, gevolgd door beëindiging van de opvolging.
- Codex-thread-heartbeat `rsl-videorotatie-opvolgen` succesvol aangemaakt, status ACTIVE, dagelijks 19:20 (Europe/Amsterdam). Geen Meta-native regel: de wissels worden door de Codex-opvolging uitgevoerd. Voor 16 oktober blijft de opvolging stil en verandert niets.
- 16 oktober: Gratis/Free uit, Je sessie/Your session aan; Waait/Is it blowing blijft uit. 20 oktober: alle zes snippets terug actief, resultaten controleren, PROJECTSTATUS bijwerken en automation op PAUSED. Elke fase eenmaal uitvoeren; recente gebruikerswijzigingen respecteren; bij toegangsproblemen melden.
- Budgetten blijven EUR 3 gemiddeld per campagne per dag (EUR 6 samen). Dit vervangt de eerdere notitie dat de scheduler geblokkeerd/niet aangemaakt was.
