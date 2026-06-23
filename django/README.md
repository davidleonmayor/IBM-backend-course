# Django — mysite

## What's in here?

```
django/
├── manage.py          # CLI tool: migrate, runserver, startapp...
├── mysite/            # PROJECT = global configuration
│   ├── settings.py    #   DB, installed apps, middleware, language...
│   ├── urls.py        #   Routes → maps URLs to views
│   ├── asgi.py        #   Entry point for async servers
│   └── wsgi.py        #   Entry point for sync servers
└── core/              # APP = actual functionality
    ├── models.py      #   Database tables
    ├── views.py       #   Logic for each route
    └── admin.py       #   Admin panel config
```

## Project vs App

Django separates **configuration** from **functionality**:

| Folder    | What it is                                                                 | Analogy                                             |
| --------- | -------------------------------------------------------------------------- | --------------------------------------------------- |
| `mysite/` | **Project** — global settings, root URLs, entry points. No business logic. | The house (walls, roof, electricity)                |
| `core/`   | **App** — models, views, tests. Where the real work happens.               | The furniture (beds, tables, what you actually use) |

You can have multiple apps inside one project (e.g., `blog`, `users`, `payments`). Each app is independent and self-contained.

## How Django works

When someone requests a URL:

```
URL → urls.py → view → response (HTML/JSON)
                         │
                    models.py (if it needs data)
```

- **View** — function or class that receives a request and returns a response. Lives inside each app.
- **Model** — Python class that represents a database table. Lives inside each app.
- **Migration** — file that syncs your models with the database.

## How to run

From the repo root:

```bash
make setup              # Create database tables
make run                # Start dev server at localhost:8000
```

Or manually with uv:

```bash
uv run python django/manage.py migrate
uv run python django/manage.py runserver
```

## Useful commands

| Command                                          | What it does                              |
| ------------------------------------------------ | ----------------------------------------- |
| `make setup`                                     | Create database tables                    |
| `make run`                                       | Start dev server                          |
| `make makemigrations`                            | Generate migrations after changing models |
| `make migrate`                                   | Apply migrations                          |
| `make shell`                                     | Interactive Django console                |
| `make createsuperuser`                           | Create admin user                         |
| `uv run python django/manage.py startapp <name>` | Create a new app                          |
