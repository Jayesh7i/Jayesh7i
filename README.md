# Jayesh7i v1

A beginner-friendly Python starter project with a clean `src/` layout, tests, CI, and learning docs.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -r requirements-dev.txt
pytest
python -m jayesh7i.cli --name Jayesh
```

## Project structure

- `src/jayesh7i/` — package code
- `tests/` — unit tests
- `docs/` — Mermaid diagrams and learning roadmap
- `.github/workflows/ci.yml` — lint + test in CI

## Learning docs

- Intro Gantt diagram: [`docs/diagrams/intro-gantt.md`](docs/diagrams/intro-gantt.md)
- French A2 roadmap: [`docs/roadmap/french-a2-mermaid.md`](docs/roadmap/french-a2-mermaid.md)
