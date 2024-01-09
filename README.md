# friByte.no

Statically generated using [Zola][zola].

## Getting started

1. Install [Zola][zola_install]
1. `git clone git@github.com:fribyte-code/fribyte.no.git`.
1. Run `zola serve` to run Zola locally in development mode.
1. Run `zola build` to build the finished website.

Use `zola --help` for more useful commands.

## Deployment

- The site is self-hosted on friByte's serveres (it's running Pengebingen).
- When you push to `main` it deploys to Pengebingen via GitHub Actions.

## Things to know

- [Zola][zola] is a static site generator.
  - Check out their [documentation][zola_docs]
  - There is a differrance between a _page_ and a _section_.
- We use [SASS][sass] for styling.
- We use [Prettier][prettier] for linting, so try to run Prettier in your editor
  (if you can).
- Navigation links is in `config.toml`.

### Git-branches

We practice feature-branches and use PRs frequently for all our features,
bugfixes and doc changes. `main`-branch is protected and should not be pushed
directly to.

Examples:

- `feature/<feature-name>`
- `bugfix/<fix-name>`
- `docs/<what-has-been-added/updated>`

### Shortcodes

We have a few shortcodes available to use in Markdown, [check them
out][shortcodes]:

- `buttons`
- `illustration`
- `alerts`

These are simple HTML-snippets that we can provide parameters:

```tera
{{ buttons(kontakt=true) }}
```

Create new shortcodes if there is a component and/or HTML-snippets that can be
used multiple places.

### News

In order to publish news we need to create a new markdown-file under
`content/nyheter`. For example: `content/nyheter/2022-01-01-godt-nyttar.md`.

If this news were to contain pictures/images, it's neccessary to create a folder
instead of a single markdown-file. Then it would look something like this:
`content/nyheter/2022-01-01-godt-nyttar/index.md`. Now it's `index.md` that
contains the _article_, and you can add the images in the same folder.

### Taxonomies

We use these for tags/categories. You can defined new taxonomies in
`config.toml`.

An example on how you can use them on _pages_ and _sections_:

```toml
[taxonomies]
categories = ["Nyheter"]
# for multiple ["Nyheter", "Driftsmelding"]
```

### Translation

The default language is Norwegian, but we are also working to add support to the
site in English. To translate a page to english, create a copy of the .md file
you want to translate, and change the extension from `.md` to `.en.md.` Then,
translate the content in the new file to english.

To translate buttons, add the argument `english=true`, like so:
`{{ buttons(tjenester=true}}` -> `{{ buttons(english=true, tjenester=true}}`

Translation not currently supported for:

- Header template
- Footer template

[zola]: https://getzola.org
[zola_install]:
  https://www.getzola.org/documentation/getting-started/installation/
[zola_docs]: https://getzola.org/documentation
[sass]: https://sass-lang.com
[prettier]: https://prettier.io/
[shortcodes]:
  https://github.com/fribyte-code/fribyte.no/tree/main/templates/shortcodes
