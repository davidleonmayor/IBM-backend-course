.DEFAULT_GOAL := run

setup:
	uv run python django/manage.py migrate

run:
	uv run python django/manage.py runserver

makemigrations:
	uv run python django/manage.py makemigrations

migrate-apply:
	uv run python django/manage.py migrate

shell:
	uv run python django/manage.py shell

createsuperuser:
	uv run python django/manage.py createsuperuser
