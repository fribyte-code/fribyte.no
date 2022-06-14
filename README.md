# friByte.no

Made using [Zola][zola].

## Usage

1. Clone the repository, `git clone git@github.com:fribyte-code/fribyte.no.git`.
2. Run `zola serve` to run Zola locally.

## Deployment

- The site is self-hosted on friByte's serveres (it's running Pengebingen).
- When you push to `main` it deploys to Pengebingen.

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

```md
{{ buttons(kontakt=true) }}
```

Create new shortcodes if there is a component and/or HTML-snippets that can be
used multiple places.

### News

In order to publish news we need to create a new markdown-file under
`content/nyheter`. For example: 
`content/nyheter/2022-01-01-godt-nyttar.md`.

If this news were to contain pictures/images, it's neccessary to create a folder
instead of a single markdown-file. Then it would look something like this:
`content/nyheter/2022-01-01-godt-nyttar/index.md`. Now it's `index.md` that
contains the _article_, and you can add the images in the same folder.

### Taxonomies

We use these for tags/categories. You can defined new taxonomies in
`config.toml`.

An example on how you can use them on _pages_ and _sections_:

```html
[taxonomies] categories = ["Nyheter"]
<!-- for multiple ["Nyheter", "Driftsmelding"] -->
```

[zola]: https://getzola.org
[zola_docs]: https://getzola.org/documentation
[sass]: https://sass-lang.com
[prettier]: https://prettier.io/
[shortcodes]: https://github.com/fribyte-code/fribyte.no/tree/main/templates/shortcodes
