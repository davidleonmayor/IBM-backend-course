# uv — Cheat Sheet

> Reemplaza `venv` + `pip` + `pip-tools` + `pyenv` + `poetry`. Todo en uno, escrito en Rust.

---

## El cambio mental más importante

```fish
# Lo viejo — sufrías con el shell
source env/bin/activate.fish
python app.py
deactivate

# Lo nuevo — uv maneja el venv por vos
uv run python app.py
```

`uv run` detecta el venv, lo crea si no existe, instala lo que falta, y ejecuta. **Nunca más activás el venv a mano.**

---

## Instalación

```fish
brew install uv
```

---

## Proyecto

```fish
uv init                      # crear proyecto nuevo (genera pyproject.toml)
uv sync                      # instalar TODO lo del proyecto (crea venv + instala)
```

---

## Paquetes

```fish
uv add flask                 # agregar un paquete
uv add pytest --dev          # agregar como dependencia de desarrollo
uv remove flask              # sacar un paquete
uv lock                      # regenerar el lockfile (uv.lock)
```

---

## Correr cosas

```fish
uv run python app.py         # correr un script
uv run flask --app x run     # correr flask
uv run pytest                # correr tests
uv run jupyter notebook      # correr jupyter
```

---

## Versiones de Python

```fish
uv python install 3.12       # instalar una versión de Python
uv python list               # ver versiones disponibles
uv python pin 3.12           # fijar versión para este proyecto
```

---

## Migrar desde pip

```fish
uv pip install -r requirements.txt   # modo compatible pip (para transición)
uv add -r requirements.txt           # importar requirements al pyproject.toml
```

---

## Utilidades

```fish
uv tree                      # ver árbol de dependencias
uv pip list                  # listar instalado
uv --version                 # verificar versión de uv
```

---

## Los 2 comandos del 90% del tiempo

| Comando | Cuándo usarlo |
|---------|---------------|
| `uv add <paquete>` | agregar una dependencia |
| `uv run <comando>` | ejecutar cualquier cosa |

---

## Archivos que genera uv

| Archivo | Qué es |
|---------|--------|
| `pyproject.toml` | config del proyecto + dependencias (commitearlo) |
| `uv.lock` | versiones exactas de todo (commitearlo) |
| `.venv/` | el entorno virtual (NO commitear, agregar a .gitignore) |
