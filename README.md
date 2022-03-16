# friByte.no - Zola

friByte sin nettside, laget med Zola.

## Quick start

```
zola serve # zola serve -O for å åpne direkte i nettleseren
```

## Oppsett

Installer [Zola](https://getzola.org)

## Deploy

Når man dytter til `main` så deployes dette live på
[fribyte.no](https://fribyte.no). Nettsiden bor på VM'en **nettsider** under
Konrad.

## Bruk

Les gjerne litt i [dokumentasjonen til Zola](https://getzola.org/documentation).

### Sider og seksjoner

I Zola så er det to forskjellige typer sider, en vanlig _side_ og en _seksjon_.

En side lever direkte i `content/`, eksempelvis `content/om.md`. En seksjon
lever i en undermappe `content/<seksjonsnavn>`, denne trenger da en `_index.md`
i sin mappe.

#### Seksjon

I en seksjon har man litt flere frontmatter variabler man kan styre, men de
viktigste å tenke på er `template` og `page_template`. Hvis alle undersidene
til seksjonen skal bruke samme template definerer man dette med `page_template`.

### Shortcodes

I Zola finnes det noe som heter shortcodes, dette kan KUN brukes i
Markdown-dokumenter. Vi har shortcodes for;

- `buttons`
- `illustration`
- `alerts`

Disse er enkle HTML-snutter som kan gi parametere, et eksempel i bruk;

```md
{{ buttons(kontakt=true) }}
```

Lag nye shortcodes hvis det er komponenter/HTML-snutter som (kan) brukes flere
steder.

### Nyheter

For å publisere nyheter så lager man bare ett nytt dokument under
`content/nyheter`. Et eksempel kan være `content/nyheter/2022-01-01-godt-nyttar.md`.
Hvis denne nyheten skal inneholde bilder osv. er det nødvendig å lage en
mappe istedenfor, for å forsette på forrige eksempel
`content/nyheter/2022-01-01-godt-nyttar/index.md`. Nå er det `index.md` som
holder selve "artikkelen", plasser alt av bilder og slik i samme mappe.

### Taxonomies

Se på dette som en form for tags eller kategorisering. Man definerer nye
taxonomies i `config.toml`. Hvis `feed = true` vil disse få en egen RSS-feed.

De defineres på side- og seksjonsnivå slik;

```html
[taxonomies] categories = ["Nyheter"]
<!-- for flere ["Nyheter", "Driftsmelding"] -->
```

### Navigasjon

Menyene, hoved og footer defineres i `config.toml`.

### Osv

Det er masse annet gøy som går an å gjøre med Zola, men dette er hva vi har til
nå. Vær flink å oppdater denne så fort man legger til mer funksjonalitet slik at
alle kan være med å holde siden oppdatert :smile:
