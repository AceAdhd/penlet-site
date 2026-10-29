"""Lager svarsidene i public/ (ett spørsmål per side, norsk og engelsk).

Kjør fra hvor som helst:  python tools/make-answers.py
Teksten står her; sidene i public/ skrives på nytt hver gang, så endre her, ikke i HTML-en.
Knappenavn må være de samme som i appen (src/i18n/nb.ts og en.ts i app-repoet).
Svaret i første avsnitt er det samme som det første svaret i FAQPage-dataene.
"""
import html
import json
from pathlib import Path

SITE = 'https://penlet.app'
PUBLIC = Path(__file__).resolve().parent.parent / 'public'
UPDATED = {'nb': '29. oktober 2026', 'en': '29 October 2026'}

PLAY_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 3.5v17l9-8.5-9-8.5Z" fill="none" stroke="currentColor" '
             'stroke-width="1.8" stroke-linejoin="round"/><path d="M13 12l3.2-3 4 2.3a.8.8 0 0 1 0 1.4l-4 2.3L13 12Z" fill="none" '
             'stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>')

UI = {
    'nb': {
        'skip': 'Hopp til innholdet', 'main_id': 'innhold', 'home_label': 'Penlet, til forsiden', 'nav': 'Hovedmeny',
        'features': 'Funksjoner', 'privacy': 'Personvern', 'privacy_url': '/personvern/', 'home': '/',
        'other_lang': 'English', 'other_code': 'en', 'updated': 'Sist oppdatert', 'footer_nav': 'Bunnmeny',
        'front': 'Forsiden', 'soon': 'Kommer snart på Google Play', 'tester': 'Bli tester',
        'tester_mail': 'mailto:support@penlet.app?subject=Jeg%20vil%20teste%20Penlet',
        'cta_text': 'Penlet er på vei til Google Play for Android. Vil du prøve den før lansering? Send en e-post, så får du en invitasjon til testen.',
        'related': 'Mer om Penlet', 'faq': 'Spørsmål og svar', 'og_image': '/assets/og.png', 'locale': 'nb_NO', 'alt_locale': 'en_US',
        'og_alt': 'Penlet: et skjema på en telefon med navn, dato, kryss og en tegnet signatur.',
    },
    'en': {
        'skip': 'Skip to content', 'main_id': 'content', 'home_label': 'Penlet, to the front page', 'nav': 'Main menu',
        'features': 'Features', 'privacy': 'Privacy', 'privacy_url': '/en/privacy/', 'home': '/en/',
        'other_lang': 'Norsk', 'other_code': 'nb', 'updated': 'Last updated', 'footer_nav': 'Footer menu',
        'front': 'Front page', 'soon': 'Coming soon on Google Play', 'tester': 'Become a tester',
        'tester_mail': 'mailto:support@penlet.app?subject=I%20want%20to%20test%20Penlet',
        'cta_text': 'Penlet is on its way to Google Play for Android. Want to try it before launch? Send us an email and we’ll invite you to the test.',
        'related': 'More about Penlet', 'faq': 'Questions and answers', 'og_image': '/assets/og-en.png', 'locale': 'en_US', 'alt_locale': 'nb_NO',
        'og_alt': 'Penlet: a form on a phone with a name, a date, a cross and a hand-drawn signature.',
    },
}

# Hver side: samme nøkkel på begge språk = hreflang-par.
PAGES = {
    'sign': {
        'nb': {
            'path': '/signere-pdf-pa-mobilen/',
            'title': 'Slik signerer du en PDF på mobilen – Penlet',
            'description': 'Åpne PDF-en i Penlet, trykk «Signatur» og tegn med fingeren – eller ta bilde av signaturen på papir. Slik signerer du en PDF på Android, uten konto og uten opplasting.',
            'h1': 'Hvordan signerer jeg en PDF på mobilen?',
            'answer': 'Åpne PDF-en i Penlet, trykk «Signatur» og trykk der signaturen skal stå. Første gang tegner du signaturen med fingeren eller tar bilde av den på et ark. Så drar du den på plass, justerer størrelsen og trykker «Lagre». Du får en ny kopi av PDF-en med signaturen, og originalen endres ikke.',
            'body': '''
  <h2>Steg for steg</h2>
  <ol>
    <li><strong>Åpne PDF-en.</strong> Trykk «Åpne PDF-fil» i Penlet, eller trykk på vedlegget i e-posten og velg Penlet under «Åpne med» eller «Del».</li>
    <li><strong>Trykk «Signatur»</strong> i verktøylinja nederst, og trykk der signaturen skal stå. Har skjemaet et eget signaturfelt, trykker du rett i feltet («Signer her»).</li>
    <li><strong>Lag signaturen.</strong> Tegn den med fingeren over hele skjermen, eller velg «Ta bilde» og fotografer signaturen din på et hvitt ark. Penlet finner signaturen, du justerer firkanten rundt den, og papiret fjernes.</li>
    <li><strong>Dra den på plass</strong> og gjør den større eller mindre. Bommer du, trykker du «Angre».</li>
    <li><strong>Trykk «Lagre».</strong> Penlet spør hvilken mappe kopien skal i, og lagrer den som «navn (Penlet).pdf». Med «Del» sender du den rett til e-post, meldinger eller en annen app.</li>
  </ol>

  <h2>Neste gang går det på ett trykk</h2>
  <p>Signaturen lagres på telefonen, så neste gang velger du «Bruk denne» i stedet for å tegne på nytt. Den lagres bare på denne telefonen og sendes ingen steder.</p>

  <h2>Signatur fra papir</h2>
  <p>Mange vil helst ha den ekte håndskriften sin. Skriv signaturen med penn på et hvitt ark, hold kameraet rett over og nært, og ta bildet. Penlet klipper ut blekket og fjerner papiret, så signaturen ligger rent på dokumentet. Du kan velge om den skal være blå, svart eller som på papiret.</p>

  <h2>Er en tegnet signatur gyldig?</h2>
  <p>Penlet setter inn signaturen du tegner eller fotograferer, i PDF-en. Det er ikke en sertifikatbasert elektronisk signatur. Mange godtar en tegnet signatur, for eksempel på kontrakter, samtykkeskjema og fullmakter, men noen dokumenter krever en egen løsning for elektronisk signering. Spør mottakeren hvis du er usikker.</p>
''',
            'faq': [
                ('Kan jeg bruke signaturen min fra papir?', 'Ja. Velg «Ta bilde» i signaturvinduet og fotografer signaturen din på et hvitt ark. Penlet finner signaturen, du justerer firkanten rundt den, og papiret fjernes.'),
                ('Er en tegnet signatur gyldig?', 'Penlet setter inn signaturen du tegner, i PDF-en. Det er ikke en sertifikatbasert elektronisk signatur. Mange godtar en tegnet signatur, men noen dokumenter krever en egen løsning for elektronisk signering. Spør mottakeren hvis du er usikker.'),
                ('Lastes PDF-en eller signaturen opp?', 'Nei. Alt skjer på telefonen. Penlet har ingen konto, og appen ber ikke engang om tilgang til internett.'),
            ],
        },
        'en': {
            'path': '/en/sign-pdf-on-phone/',
            'title': 'How to sign a PDF on your phone – Penlet',
            'description': 'Open the PDF in Penlet, tap “Signature” and draw with your finger – or take a photo of your signature on paper. How to sign a PDF on Android, with no account and no upload.',
            'h1': 'How do I sign a PDF on my phone?',
            'answer': 'Open the PDF in Penlet, tap “Signature” and tap where the signature should go. The first time, you draw your signature with your finger or take a photo of it on a sheet of paper. Then you drag it into place, adjust the size and tap “Save”. You get a new copy of the PDF with your signature, and the original is not changed.',
            'body': '''
  <h2>Step by step</h2>
  <ol>
    <li><strong>Open the PDF.</strong> Tap “Open PDF file” in Penlet, or tap the attachment in your email and choose Penlet under “Open with” or “Share”.</li>
    <li><strong>Tap “Signature”</strong> in the toolbar at the bottom, and tap where the signature should go. If the form has a signature field, tap the field itself (“Sign here”).</li>
    <li><strong>Make your signature.</strong> Draw it with your finger across the whole screen, or choose “Take photo” and photograph your signature on a sheet of white paper. Penlet finds the signature, you adjust the box around it, and the paper is removed.</li>
    <li><strong>Drag it into place</strong> and make it bigger or smaller. If you slip, tap “Undo”.</li>
    <li><strong>Tap “Save”.</strong> Penlet asks which folder the copy should go in and saves it as “name (Penlet).pdf”. Tap “Share” to send it straight to email, messages or another app.</li>
  </ol>

  <h2>Next time it takes one tap</h2>
  <p>Your signature is kept on your phone, so next time you choose “Use this one” instead of drawing it again. It is stored only on this phone and is never sent anywhere.</p>

  <h2>A signature from paper</h2>
  <p>Many people prefer their real handwriting. Sign with a pen on a sheet of white paper, hold the camera straight above and close, and take the picture. Penlet cuts out the ink and removes the paper, so the signature sits cleanly on the document. You can make it blue, black or keep it as on paper.</p>

  <h2>Is a drawn signature valid?</h2>
  <p>Penlet places the signature you draw or photograph into the PDF. It is not a certificate-based electronic signature. Many recipients accept a drawn signature, for example on contracts, consent forms and powers of attorney, but some documents require a dedicated e-signing service. Ask the recipient if you’re unsure.</p>
''',
            'faq': [
                ('Can I use my signature from paper?', 'Yes. Choose “Take photo” in the signature window and photograph your signature on a sheet of white paper. Penlet finds the signature, you adjust the box around it, and the paper is removed.'),
                ('Is a drawn signature valid?', 'Penlet places the signature you draw into the PDF. It is not a certificate-based electronic signature. Many recipients accept a drawn signature, but some documents require a dedicated e-signing service. Ask the recipient if you’re unsure.'),
                ('Is the PDF or my signature uploaded?', 'No. Everything happens on your phone. Penlet has no account, and the app does not even request internet access.'),
            ],
        },
    },
    'fill': {
        'nb': {
            'path': '/fylle-ut-pdf-skjema-pa-mobilen/',
            'title': 'Slik fyller du ut et PDF-skjema på mobilen – Penlet',
            'description': 'Fyll ut PDF-skjema på Android – også flate skjema uten felt og skjema du har tatt bilde av. Penlet finner rutene og linjene selv, så du bare trykker og skriver.',
            'h1': 'Hvordan fyller jeg ut et PDF-skjema på mobilen?',
            'answer': 'Åpne skjemaet i Penlet og trykk i feltene. Har PDF-en utfyllbare felt, skriver du rett i dem og krysser av i rutene. Er skjemaet flatt, altså uten felt å trykke i, finner Penlet rutene og skrivelinjene selv, så du fyller ut på samme måte. Til slutt trykker du «Lagre» og får en utfylt kopi.',
            'body': '''
  <h2>Skjema med utfyllbare felt</h2>
  <p>Mange PDF-skjema fra kommuner, skoler og firmaer har ekte skjemafelt. Dem fyller du ut direkte i Penlet: tekstfelt, avkrysningsruter, radioknapper og lister. Verdiene skrives inn i feltene i kopien du lagrer, så mottakeren ser dem i hvilken som helst PDF-leser.</p>

  <h2>Skjema uten felt</h2>
  <p>Et trykt skjema som er gjort om til PDF, har ofte bare streker og ruter, ingen felt. Penlet ser etter rutene og skrivelinjene på siden og gjør dem om til felt du kan trykke i, med navnet som står ved siden av. Det virker også på papirskjema du har tatt bilde av.</p>
  <ul>
    <li>Finner ikke Penlet et felt, velger du «Tekst», «Kryss», «Hake» eller «Dato» og trykker der det skal stå.</li>
    <li>Har den funnet et felt som ikke er et felt, holder du fingeren på det for å fjerne det. «Angre» henter det tilbake.</li>
    <li>Når du lagrer, blir feltene ekte skjemafelt i kopien.</li>
  </ul>

  <h2>Dato, kryss og hake</h2>
  <p>Datoen velger du i en kalender, eller du skriver den selv. Den skrives slik telefonen din skriver datoer. Kryss og hake setter du hvor som helst, og alt du har plassert, kan flyttes, gjøres større eller mindre og slettes etterpå.</p>

  <h2>Fortsett senere</h2>
  <p>Endringene lagres fortløpende som en kladd på telefonen. Lukker du appen midt i, ligger skjemaet under «Dokumenter» til du er ferdig.</p>

  <h2>Til slutt: signer og send</h2>
  <p>Skal skjemaet signeres, gjør du det i samme omgang – se <a href="/signere-pdf-pa-mobilen/">hvordan du signerer en PDF på mobilen</a>. Trykk så «Lagre», og «Del» for å sende kopien.</p>
''',
            'faq': [
                ('Skjemaet mitt har ingen felt å trykke i. Kan jeg fylle det ut likevel?', 'Ja. Penlet finner rutene og skrivelinjene i et trykt skjema selv, så du bare trykker i dem og skriver. Det virker også på skjema du har tatt bilde av. Finner den ikke et felt, trykker du der teksten skal stå og skriver.'),
                ('Ser mottakeren det jeg har fylt ut?', 'Ja. Penlet lagrer en ny kopi av PDF-en med verdiene i skjemafeltene, så de vises i hvilken som helst PDF-leser. Originalen endres ikke.'),
                ('Kan jeg fortsette å fylle ut senere?', 'Ja. Endringene lagres som en kladd på telefonen, og skjemaet ligger under «Dokumenter» til du er ferdig.'),
            ],
        },
        'en': {
            'path': '/en/fill-in-pdf-form-on-phone/',
            'title': 'How to fill in a PDF form on your phone – Penlet',
            'description': 'Fill in PDF forms on Android – including flat forms with no fields and forms you have photographed. Penlet finds the boxes and lines itself, so you just tap and type.',
            'h1': 'How do I fill in a PDF form on my phone?',
            'answer': 'Open the form in Penlet and tap the fields. If the PDF has fillable fields, you type straight into them and tick the boxes. If the form is flat, with no fields to tap, Penlet finds the boxes and lines itself, so you fill it in the same way. When you’re done, tap “Save” to get a filled-in copy.',
            'body': '''
  <h2>Forms with fillable fields</h2>
  <p>Many PDF forms from councils, schools and companies have real form fields. You fill them in directly in Penlet: text fields, checkboxes, radio buttons and lists. The values are written into the fields of the copy you save, so the recipient sees them in any PDF reader.</p>

  <h2>Forms with no fields</h2>
  <p>A printed form turned into a PDF often has only lines and boxes, no fields. Penlet looks for the boxes and writing lines on the page and turns them into fields you can tap, named after the label next to them. It works on paper forms you have photographed too.</p>
  <ul>
    <li>If Penlet misses a field, choose “Text”, “Cross”, “Check” or “Date” and tap where it should go.</li>
    <li>If it found something that isn’t a field, press and hold it to remove it. “Undo” brings it back.</li>
    <li>When you save, the fields become real form fields in the copy.</li>
  </ul>

  <h2>Dates, crosses and ticks</h2>
  <p>You pick a date in a calendar, or type it yourself. It is written the way your phone writes dates. Crosses and ticks go anywhere, and everything you place can be moved, resized and deleted afterwards.</p>

  <h2>Finish later</h2>
  <p>Your changes are kept as a draft on the phone as you go. If you close the app halfway, the form waits under “Documents” until you’re done.</p>

  <h2>Finally: sign and send</h2>
  <p>If the form needs a signature, add it in the same go – see <a href="/en/sign-pdf-on-phone/">how to sign a PDF on your phone</a>. Then tap “Save”, and “Share” to send the copy.</p>
''',
            'faq': [
                ('My form has no fields to tap. Can I still fill it in?', 'Yes. Penlet finds the boxes and lines in a printed form by itself, so you just tap them and type. It works on forms you have photographed too. If it misses a field, tap where the text should go and type.'),
                ('Will the recipient see what I filled in?', 'Yes. Penlet saves a new copy of the PDF with the values in the form fields, so they show in any PDF reader. The original is not changed.'),
                ('Can I finish filling it in later?', 'Yes. Your changes are kept as a draft on the phone, and the form waits under “Documents” until you’re done.'),
            ],
        },
    },
    'photo': {
        'nb': {
            'path': '/ta-bilde-av-dokument-til-pdf/',
            'title': 'Slik gjør du et papirdokument om til PDF med mobilen – Penlet',
            'description': 'Ta bilde av papirark med mobilen og få en søkbar PDF – flere sider i én omgang. Penlet finner arket, retter det opp og renser bakgrunnen, alt på telefonen.',
            'h1': 'Hvordan gjør jeg et papirdokument om til PDF med mobilen?',
            'answer': 'Trykk «Ta bilde av dokument» i Penlet og ta bilde av arket. Penlet finner kantene på arket, retter det opp og renser bakgrunnen. Har dokumentet flere sider, trykker du «Ta bilde av neste side». Når du er ferdig, får du én PDF med alle sidene, med tekst du kan søke i.',
            'body': '''
  <h2>Steg for steg</h2>
  <ol>
    <li><strong>Trykk «Ta bilde av dokument»</strong> på forsiden av Penlet. Velg «Ta bilde», eller «Fra bilder» hvis du allerede har tatt bildet.</li>
    <li><strong>Sjekk hjørnene.</strong> Penlet finner arket selv. Er det noe som ikke stemmer, drar du i hjørnene. «Roter» snur siden.</li>
    <li><strong>Velg utseende:</strong> «Dokument», «Gråtone», «Svart-hvitt» eller «Foto». Trykk «Bruk».</li>
    <li><strong>Flere sider?</strong> Trykk «Ta bilde av neste side» og fortsett. Til slutt trykker du «Ferdig».</li>
  </ol>
  <p>Sidene blir A4, stående eller liggende etter arket. Skjev tekst rettes opp, og bakgrunnen rundt arket skjæres bort.</p>

  <h2>Tekst du kan søke i</h2>
  <p>Penlet leser teksten på bildet og legger den usynlig under, så du kan søke i PDF-en og kopiere fra den. Tekstgjenkjenningen kjører på telefonen i Google Play-tjenester. Første gang kan Google laste ned språkmodellen, og da trengs nett.</p>

  <h2>Fyll ut og signer med en gang</h2>
  <p>Var det et skjema, finner Penlet rutene og skrivelinjene på bildet, så du kan <a href="/fylle-ut-pdf-skjema-pa-mobilen/">fylle det ut</a> og <a href="/signere-pdf-pa-mobilen/">signere det</a> før du sender det tilbake.</p>

  <h2>Glemte du en side?</h2>
  <p>Åpne «Sider» i dokumentet og trykk «Ta bilde av flere sider». Der kan du også flytte, rotere og slette sider.</p>
''',
            'faq': [
                ('Blir PDF-en søkbar?', 'Ja. Penlet leser teksten på bildet og legger den usynlig under siden, så du kan søke i dokumentet. Tekstgjenkjenningen kjører på telefonen.'),
                ('Sendes bildene til en server?', 'Nei. Bildene behandles på telefonen og slettes fra appens mellomlager rett etter at de er lest inn. Tekstgjenkjenningen kjører på telefonen i Google Play-tjenester, og bildene sendes ikke til Google.'),
                ('Kan jeg bruke bilder jeg allerede har tatt?', 'Ja. Velg «Fra bilder» i stedet for «Ta bilde», så behandles bildet på samme måte.'),
            ],
        },
        'en': {
            'path': '/en/photo-to-pdf/',
            'title': 'How to turn a paper document into a PDF with your phone – Penlet',
            'description': 'Take photos of paper sheets with your phone and get a searchable PDF – several pages in one go. Penlet finds the sheet, straightens it and cleans up the background, all on the phone.',
            'h1': 'How do I turn a paper document into a PDF with my phone?',
            'answer': 'Tap “Take photo of document” in Penlet and take a picture of the sheet. Penlet finds the edges of the sheet, straightens it and cleans up the background. If the document has more pages, tap “Take photo of next page”. When you’re done, you get one PDF with all the pages, with text you can search.',
            'body': '''
  <h2>Step by step</h2>
  <ol>
    <li><strong>Tap “Take photo of document”</strong> on Penlet’s front page. Choose “Take photo”, or “From photos” if you already took the picture.</li>
    <li><strong>Check the corners.</strong> Penlet finds the sheet by itself. If something is off, drag the corners. “Rotate” turns the page.</li>
    <li><strong>Choose a look:</strong> “Document”, “Grayscale”, “Black &amp; white” or “Photo”. Tap “Use”.</li>
    <li><strong>More pages?</strong> Tap “Take photo of next page” and carry on. Tap “Done” at the end.</li>
  </ol>
  <p>The pages become A4, portrait or landscape to match the sheet. Skewed text is straightened, and the background around the sheet is cut away.</p>

  <h2>Text you can search</h2>
  <p>Penlet reads the text in the picture and places it invisibly underneath, so you can search the PDF and copy from it. Text recognition runs on the phone in Google Play services. The first time, Google may download the language model, and that needs internet.</p>

  <h2>Fill in and sign right away</h2>
  <p>If it was a form, Penlet finds the boxes and writing lines in the picture, so you can <a href="/en/fill-in-pdf-form-on-phone/">fill it in</a> and <a href="/en/sign-pdf-on-phone/">sign it</a> before you send it back.</p>

  <h2>Forgot a page?</h2>
  <p>Open “Pages” in the document and tap “Take photos of more pages”. There you can also move, rotate and delete pages.</p>
''',
            'faq': [
                ('Is the PDF searchable?', 'Yes. Penlet reads the text in the picture and places it invisibly under the page, so you can search the document. Text recognition runs on the phone.'),
                ('Are the photos sent to a server?', 'No. The photos are processed on the phone and deleted from the app’s cache right after they are read. Text recognition runs on the phone in Google Play services, and the photos are not sent to Google.'),
                ('Can I use photos I have already taken?', 'Yes. Choose “From photos” instead of “Take photo”, and the picture is processed the same way.'),
            ],
        },
    },
}

ORDER = ['sign', 'fill', 'photo']


def esc(s):
    return html.escape(s, quote=True)


def page_html(key, lang):
    p = PAGES[key][lang]
    other = 'en' if lang == 'nb' else 'nb'
    o = PAGES[key][other]
    ui = UI[lang]
    url = SITE + p['path']
    nb_url = SITE + PAGES[key]['nb']['path']
    en_url = SITE + PAGES[key]['en']['path']

    faq = [(p['h1'], p['answer'])] + p['faq']
    ld = {
        '@context': 'https://schema.org',
        '@graph': [
            {
                '@type': 'WebPage', '@id': url + '#page', 'url': url, 'name': p['title'],
                'description': p['description'], 'inLanguage': lang,
                'isPartOf': {'@id': SITE + '/#website'}, 'about': {'@id': SITE + '/#app'},
                'publisher': {'@id': SITE + '/#org'},
            },
            {
                '@type': 'FAQPage', '@id': url + '#faq', 'inLanguage': lang,
                'mainEntity': [
                    {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq
                ],
            },
        ],
    }
    ld_json = json.dumps(ld, ensure_ascii=False, indent=2).replace('</', '<\\/')

    faq_html = '\n'.join(f'  <h3>{esc(q)}</h3>\n  <p>{esc(a)}</p>' for q, a in p['faq'])
    related = '\n'.join(
        f'    <li><a href="{PAGES[k][lang]["path"]}">{esc(PAGES[k][lang]["h1"])}</a></li>' for k in ORDER if k != key
    )
    related += f'\n    <li><a href="{ui["home"]}#funksjoner">{esc(ui["features"])}</a></li>' if lang == 'nb' else \
               f'\n    <li><a href="{ui["home"]}#features">{esc(ui["features"])}</a></li>'

    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p['title'])}</title>
<meta name="description" content="{esc(p['description'])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="nb" href="{nb_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta name="theme-color" content="#f4f6fb" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0f1420" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/assets/icon-48.png" sizes="48x48" type="image/png">
<link rel="apple-touch-icon" href="/assets/icon-180.png">
<link rel="stylesheet" href="/assets/site.css">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Penlet">
<meta property="og:locale" content="{ui['locale']}">
<meta property="og:locale:alternate" content="{ui['alt_locale']}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(p['h1'])}">
<meta property="og:description" content="{esc(p['description'])}">
<meta property="og:image" content="{SITE}{ui['og_image']}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(ui['og_alt'])}">
<meta name="twitter:card" content="summary_large_image">

<script type="application/ld+json">
{ld_json}
</script>
</head>
<body>
<a class="skip" href="#{ui['main_id']}">{esc(ui['skip'])}</a>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{ui['home']}" aria-label="{esc(ui['home_label'])}">
      <img src="/assets/icon.png" alt="" width="36" height="36">
      <span>Penlet</span>
    </a>
    <nav class="nav" aria-label="{esc(ui['nav'])}">
      <a class="hide-sm" href="{ui['home']}#{'funksjoner' if lang == 'nb' else 'features'}">{esc(ui['features'])}</a>
      <a href="{ui['privacy_url']}">{esc(ui['privacy'])}</a>
      <a class="lang" href="{o['path']}" hreflang="{other}" lang="{other}">{esc(ui['other_lang'])}</a>
    </nav>
  </div>
</header>

<main id="{ui['main_id']}" class="doc">
<div class="wrap">
  <h1>{esc(p['h1'])}</h1>
  <p class="answer">{esc(p['answer'])}</p>
{p['body']}
  <h2>{esc(ui['faq'])}</h2>
{faq_html}

  <div class="summary get">
    <p>{esc(ui['cta_text'])}</p>
    <div class="cta">
      <span class="btn btn-soon" aria-disabled="true">
        {PLAY_ICON}
        {esc(ui['soon'])}
      </span>
      <a class="btn btn-primary" href="{ui['tester_mail']}">{esc(ui['tester'])}</a>
    </div>
  </div>

  <h2>{esc(ui['related'])}</h2>
  <ul class="related">
{related}
  </ul>
  <p class="updated">{esc(ui['updated'])} {UPDATED[lang]}</p>
</div>
</main>

<footer class="site-footer">
  <div class="wrap">
    <span>© 2026 Trolda AS · <a href="mailto:support@penlet.app">support@penlet.app</a></span>
    <nav aria-label="{esc(ui['footer_nav'])}">
      <a href="{ui['home']}">{esc(ui['front'])}</a>
      <a href="{ui['privacy_url']}">{esc(ui['privacy'])}</a>
      <a href="{o['path']}" hreflang="{other}" lang="{other}">{esc(ui['other_lang'])}</a>
    </nav>
  </div>
</footer>
</body>
</html>
'''


def main():
    for key in ORDER:
        for lang in ('nb', 'en'):
            out = PUBLIC / PAGES[key][lang]['path'].strip('/') / 'index.html'
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(page_html(key, lang), encoding='utf-8', newline='\n')
            print('skrev', out.relative_to(PUBLIC.parent))


if __name__ == '__main__':
    main()
