# AGENTS.md

## What this repo is

Learning/course repository for IBM backend course — **not** a production app. Contains independent sub-projects, not a monorepo with shared build.

## Package manager

**uv** — never `pip install` directly. Use `uv run <cmd>` to execute anything inside the managed venv. Never activate `.venv/` manually.

```bash
uv sync              # install all deps (creates venv if needed)
uv add <pkg>         # add a dependency
uv run python app.py # run scripts
uv run pytest        # run tests (none exist yet)
```

## Structure

| Directory | What it is |
|-----------|------------|
| `django/mysite/` | Bare Django skeleton (manage.py, settings, urls) — no apps yet |
| `flask/` | Minimal Flask app. Loads secrets from `flask/.env` via `python-dotenv`. |
| `Python-for-Data-Science-AI-And-Develpment/` | Jupyter notebooks + CSV data files for data science exercises |
| `bash/scripting/` | Shell script exercises |
| `main.py` | Placeholder entrypoint |

## Gotchas

- `requirements.txt` is **stale/legacy** — real deps are in `pyproject.toml` + `uv.lock`. Do not pip-install from it.
- `.python-version` says 3.14, `pyproject.toml` requires `>=3.12`. They're compatible but verify with `python --version` if something breaks.
- `flask/.env` contains secrets — never read or commit it.
- No lint, typecheck, test, or CI pipelines are configured. `NEED.md` lists aspirational tooling but it's not wired up yet.
- The `Makefile` is empty — no make targets exist.
