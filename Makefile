PROJECT_DIR=$(shell pwd)
VENV_DIR=$(PROJECT_DIR)/env
PIP=$(VENV_DIR)/bin/pip
PYTHON=$(VENV_DIR)/bin/python

all: virtualenv pip

virtualenv:
	virtualenv -p python3 $(VENV_DIR)

pip: requirements requirements-dev

requirements:
	$(PIP) install --upgrade pip
	$(PIP) install -r $(PROJECT_DIR)/requirements.txt

requirements-dev:
	$(PIP) install -r $(PROJECT_DIR)/requirements-dev.txt

clean: clean_venv

clean_venv:
	rm -rf $(VENV_DIR)

migrate:
	$(PYTHON) $(PROJECT_DIR)/manage.py makemigrations
	$(PYTHON) $(PROJECT_DIR)/manage.py migrate	

test:
	$(PYTHON) $(PROJECT_DIR)/manage.py test

jenkins:
	$(PYTHON) $(PROJECT_DIR)/manage.py jenkins
