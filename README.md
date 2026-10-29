# penlet.app

Nettsiden for appen Penlet (PDF: fylle ut, signere og ordne sider; appen ligger i `X:\App Prodjects\Ark`, app-id `no.arkpdf.app`). Ren HTML og CSS, ingen JavaScript, ingen byggesteg. All bevegelse er CSS: skjemaet i hero-en fylles ut med keyframes, resten er scroll-drevne animasjoner (`animation-timeline: view()`) bak `@supports`, så nettlesere uten støtte viser siden stille. `prefers-reduced-motion` skrur bevegelsen av.

## Mapper

- `public/` – alt som publiseres. Last opp denne mappen og ingenting annet.
  - `index.html` – forsiden på norsk
  - `personvern/` – personvernerklæringen (lenkes fra Google Play)
  - `en/` og `en/privacy/` – engelsk
  - svarsider (ett spørsmål per side): `signere-pdf-pa-mobilen/`, `fylle-ut-pdf-skjema-pa-mobilen/`, `ta-bilde-av-dokument-til-pdf/` og de engelske under `en/`. **Lages av `python tools/make-answers.py`** – endre teksten der, ikke i HTML-en. Knappenavnene skal være de samme som i appen (`src/i18n/nb.ts`/`en.ts`). Ny svarside: legg den i skriptet, i `sitemap.xml`, `llms.txt` og bunnmenyen på forsidene.
  - `404.html`, `robots.txt`, `sitemap.xml`, `site.webmanifest`, `llms.txt`
  - `<nøkkel>.txt` – IndexNow-nøkkelen (samme som `tools/indexnow-key.txt`)
  - `assets/` – stilark, skrifter (lokale, OFL), ikon og delingsbilder
- `tools/` – maler for delingsbildene (`og.png`, `og-en.png`). Kjør `sh render.sh` i `tools/` etter at tekst eller design er endret. Ikonene lages av `python make-icons.py` i `tools/` fra `penlet-icon.webp` (det offisielle Penlet-ikonet, samme fil som `store/penlet-icon.webp` i app-repoet) – ikke tegn ikoner for hånd. `_headers.cloudflare` er sikkerhetshoder til bruk hvis siden flyttes til Cloudflare Pages eller Netlify (GitHub Pages leser dem ikke).

## Se siden lokalt

```bash
python -m http.server 8765 --directory public
```

Åpne http://localhost:8765.

## Publisering (GitHub Pages)

Repoet `AceAdhd/penlet-site` publiserer `public/` automatisk ved hver push til `main` (`.github/workflows/pages.yml`). Egendefinert domene `penlet.app` og «Enforce HTTPS» er satt i repoets Settings → Pages.

DNS hos GoDaddy (domenet `penlet.app`):

| Type | Navn | Verdi |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| AAAA | @ | 2606:50c0:8000::153, 2606:50c0:8001::153, 2606:50c0:8002::153, 2606:50c0:8003::153 |
| CNAME | www | aceadhd.github.io |

`www.penlet.app` sendes automatisk videre til `penlet.app`.

Etter endringer som påvirker sider: varsle Bing/IndexNow med
`node ~/.claude/skills/seo-oppsett/scripts/indexnow.mjs --site https://penlet.app --key $(cat tools/indexnow-key.txt)`.

## Når appen er publisert i Google Play

Bytt ut `<span class="btn btn-soon">` i `public/index.html` og `public/en/index.html` med en lenke til
`https://play.google.com/store/apps/details?id=no.arkpdf.app`.

## Må stemme med appen

- Personvernerklæringen er den samme som `store/personvern.md` og `store/privacy.md` i app-repoet (pluss avsnitt om krasjrapporter, kontakt, nettstedet og rettigheter). Endres det hva appen lagrer eller sender, må begge steder oppdateres samtidig, og datoen øverst endres.
- Funksjonslisten følger butikkteksten i `store/play-listing.md` i app-repoet. Ordet «skann» brukes ikke: skriv «ta bilde av».
- Prismodellen er «prøv gratis, betal bare når du trenger det» (2 dokumenter gratis, så tilgang i Google Play for 1 måned eller 12 måneder, aldri automatisk fornyelse, oppgradering fra måned til 12 måneder for mellomlegget). Beløpet står ikke på siden, fordi det varierer per land og vises i Google Play.
- Utviklernavnet i «Hvem som står bak» (Trolda AS) må være det samme som i Google Play Console. Kontaktadressen er support@penlet.app (alias på daniel@trolda.com i Zoho) – samme som i butikkens `privacy.md`/`personvern.md` og Play Console.
- Ordlyd om signatur: «Tegn signaturen din og sett den inn i en PDF.» Ikke «juridisk bindende» eller lignende.
