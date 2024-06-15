lint:
	poetry run flake8 task_manager

test:
	poetry run python3 manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report
	poetry run coverage xml

install:
	poetry install

selfcheck:
	poetry check

check: selfcheck test test-coverage lint

dev:
	poetry run python manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn -w 2 -b 0.0.0.0:8000 task_manager.wsgi

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

translate:
	poetry run python manage.py makemessages -l ru --ignore .venv

shell:
	poetry run python manage.py shell_plus --ipython

makemessages:
	 django-admin makemessages --ignore="static" --ignore=".env" -l ru

compile_translations:
	poetry run python manage.py compilemessages --ignore .venv

compilemessages:
	django-admin compilemessages