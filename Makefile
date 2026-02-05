.PHONY: help dotenv python-setup npm-setup k8s-setup compose complete

VERSION := 1.4.2
VENV	:= venv

ifeq ($(OS),Windows_NT)
	BIN := $(VENV)/Scripts
else
	BIN := $(VENV)/BIN
endif

PYTHON 	  := $(BIN)/python
PIP	   	  := $(BIN)/pip
GREEN  	  := $(shell printf "\033[0;32m")
RESET  	  := $(shell printf "\033[0m")
CHECKMARK := \342\234\223

help:
	@echo ""
	@echo "======================================================================================="
	@echo "Informations"
	@echo "Name: $(GREEN)Conteneurisation-Orchestration$(RESET)"
	@echo "Version: $(GREEN)$(VERSION)$(RESET)"
	@echo "OS: $(GREEN)$(OS)$(RESET)"
	@echo "======================================================================================="
	@echo "Commands"
	@echo "$(GREEN)dotenv$(RESET): remove and creates dotenv with values"
	@echo "$(GREEN)python-setup$(RESET): clean, creates venv, upgrade pip and install dependencies"
	@echo "$(GREEN)npm-setup$(RESET): install npm dependencies"
	@echo "$(GREEN)k8s-setup$(RESET): setup k8s, kind..."
	@echo "$(GREEN)compose$(RESET): remove builds and then compose again"
	@echo "$(GREEN)complete$(RESET): complete setup"
	@echo "======================================================================================="
	@echo ""

dotenv:
	@echo "Creating and filling .env"
	@echo "=============== WARNING - REMOVING .ENV ==============="
	rm -f .env
	touch .env
	echo MONGO_ADM_USER= >> .env
	echo MONGO_USER= >> .env 
	echo MONGO_ADM_PASSWD= >> .env
	echo MONGO_PASSWD= >> .env
	echo MONGO_URI= >> .env
	echo ADM_MONGO_URI= >> .env
	echo REACT_APP_API_URL= >> .env

python-setup:
	@echo "Setup python"
	rm -rf venv .cache logs
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete
	python -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e .
	$(PYTHON) -m pip install -e ".[dev]"

npm-setup:
	@echo "Setup npm"
	cd frontend/
	npm install

k8s-setup:
	@echo "Setup k8s"
# Install kind...

compose:
	@echo "Composing the project"
	docker compose down -v 
	docker compose up

complete: python-setup npm-setup k8s-setup compose
	@echo "Running complete project"
	@echo "You might wanna run the 'make dotenv' command and fill its values before running this."