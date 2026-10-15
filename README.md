# Clinical NLP: From Notes to Evidence

A developing [Quarto](https://quarto.org/) book about clinical natural language processing, with interactive [marimo](https://marimo.io/) examples. Read the [published book](https://schorndorfer.github.io/clinical-nlp-book/). All example notes are fictional and synthetic. **Do not use real patient data in these notebooks.** The exercises are not validated for clinical use.

## Requirements

- Quarto (for the book)
- Python 3.12+ and [uv](https://docs.astral.sh/uv/) (for the notebooks)

## Read and run

```bash
quarto preview        # local book preview
quarto render         # static HTML in _book/
uv sync               # install the Python environment
uv run marimo edit notebooks/01_assertions.py  # interactive example
uv run notebooks/01_assertions.py               # noninteractive smoke test
uv run marimo check notebooks/01_assertions.py  # notebook lint
```

Pushing to `main` runs `.github/workflows/pages.yml` to render and publish the book to GitHub Pages. Quarto renders the prose, tables, and notebook links but does not execute marimo. Run the linked notebooks separately for interactive exercises. This keeps the published book reproducible without fetching datasets or connecting to external services.

## Contents

- `index.qmd`: scope, audience, and reading guide
- `chapters/`: task definition, assertion baseline, and evaluation
- `notebooks/01_assertions.py`: reactive cue-window experiment on synthetic notes

Future topics may include terminology, de-identification, temporal reasoning, statistical models, and deployment. For work with real notes, obtain institutional approval and follow applicable privacy, security, and data-use policies.
