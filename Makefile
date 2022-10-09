VIRTUAL_ENV?=venv
PIP=$(VIRTUAL_ENV)/bin/pip
PIP_COMPILE=$(VIRTUAL_ENV)/bin/pip-compile
PYTHON_MAJOR_VERSION=3
PYTHON_MINOR_VERSION=8
PYTHON_VERSION=$(PYTHON_MAJOR_VERSION).$(PYTHON_MINOR_VERSION)
PYTHON_WITH_VERSION=python$(PYTHON_VERSION)
PYTHON=$(VIRTUAL_ENV)/bin/python
ISORT=$(VIRTUAL_ENV)/bin/isort
FLAKE8=$(VIRTUAL_ENV)/bin/flake8
BLACK=$(VIRTUAL_ENV)/bin/black
PYTEST=$(VIRTUAL_ENV)/bin/pytest
GUNICORN=$(VIRTUAL_ENV)/bin/gunicorn
DOCKER_IMAGE=andremiras/gitpop2
PORT?=8000
SOURCES=gitpop2/ tests/
ifndef CI
DOCKER_IT=-it
endif


all: virtualenv

$(VIRTUAL_ENV):
	$(PYTHON_WITH_VERSION) -m venv $(VIRTUAL_ENV)
	$(PYTHON) -m pip install --upgrade pip setuptools

virtualenv: $(VIRTUAL_ENV)
	$(PIP) install --requirement requirements.txt

requirements.txt: | $(VIRTUAL_ENV)
	$(PYTHON) -m pip install --upgrade pip-tools
	$(PIP_COMPILE) --upgrade --output-file requirements.txt requirements.in

clean:
	rm -rf venv/ .pytest_cache/

unittest: virtualenv
	$(PYTEST) tests/

lint/isort: virtualenv
	$(ISORT) --check-only --diff $(SOURCES)

lint/flake8: virtualenv
	$(FLAKE8) $(SOURCES)

lint/black: virtualenv
	$(BLACK) --check $(SOURCES)

lint: lint/isort lint/flake8 lint/black

format/isort: virtualenv
	$(ISORT) $(SOURCES)

format/black: virtualenv
	$(BLACK) $(SOURCES)

format: format/isort format/black

test: unittest lint

run/collectstatic: virtualenv
	$(PYTHON) manage.py collectstatic --noinput

run/migrate: virtualenv
	$(PYTHON) manage.py migrate --noinput

run/dev: virtualenv
	$(PYTHON) manage.py runserver

run/gunicorn: virtualenv
	$(GUNICORN) gitpop2.wsgi:application --bind 0.0.0.0:$(PORT)

docker/build:
	docker build --tag=$(DOCKER_IMAGE) .

docker/run/make/%:
	docker run --env-file .env $(DOCKER_IT) --rm $(DOCKER_IMAGE) make $*

docker/run/test: docker/run/make/test

docker/run/app:
	docker run --env-file .env --env PORT=$(PORT) --publish $(PORT):$(PORT) $(DOCKER_IT) --rm $(DOCKER_IMAGE)

docker/run/app/production:
	PRODUCTION=1 DJANGO_SECRET_KEY=1 \
	docker run --env-file .env --env PORT=$(PORT) --publish $(PORT):$(PORT) $(DOCKER_IT) --rm $(DOCKER_IMAGE)

docker/run/shell:
	docker run --env-file .env $(DOCKER_IT) --rm $(DOCKER_IMAGE) /bin/bash
