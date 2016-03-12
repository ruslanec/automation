PROJECT_DIR=$(shell pwd)
VENV_DIR=$(PROJECT_DIR)/env
PIP=$(VENV_DIR)/bin/pip
PYTHON=$(VENV_DIR)/bin/python

all: virtualenv distribute pip

virtualenv:
	virtualenv $(VENV_DIR)

distribute:
	$(PIP) install distribute

pip: requirements requirements-dev

requirements:
	$(PIP) install -r $(PROJECT_DIR)/requirements.txt

requirements-dev:
	$(PIP) install -r $(PROJECT_DIR)/requirements-dev.txt

clean: clean_venv

clean_venv:
	rm -rf $(VENV_DIR)

test:
	$(PYTHON) $(PROJECT_DIR)/manage.py test
