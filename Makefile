.PHONY: help dotenv python-setup npm-setup minikube k8s-setup compose complete

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

minikube:
	@echo "Checking kubectl installation"
	@if command -v kubectl > /dev/null 2>&1; then \
		echo "$(GREEN)V$(RESET) kubectl is already installed"; \
	else \
		echo "kubectl is not installed. Please install kubectl first."; \
		exit 1; \
	fi
	@echo "Checking minikube installation"
	@if command -v minikube > /dev/null 2>&1; then \
		echo "$(GREEN)V$(RESET) minikube is already installed"; \
	else \
		echo "minikube is not installed. Installing..."; \
		if [ "$(OS)" = "Windows_NT" ]; then \
			choco install minikube; \
		else \
			brew install minikube; \
		fi; \
	fi

k8s-setup: minikube
	@echo "Setup k8s"
	minikube start
	@echo "Building images in minikube docker environment"
	eval $$(minikube docker-env) && \
		docker build -f backend/Dockerfile -t ghcr.io/mathieuaudibert/conteneurisation-orchestration-backend:latest . && \
		docker build -t ghcr.io/mathieuaudibert/conteneurisation-orchestration-frontend:latest ./frontend && \
		docker build -f documentation/Dockerfile -t ghcr.io/mathieuaudibert/conteneurisation-orchestration-documentation:latest .
	@echo "applying secrets from .env"
	@if [ ! -f .env ]; then \
		echo "Error: .env file not found. Run 'make dotenv' first."; \
		exit 1; \
	fi
	@. ./.env && envsubst < k8s/secrets.yml | kubectl apply -f -
	@echo "deploying mongodb pod"
	kubectl apply -f k8s/mongoDB.yml
	kubectl wait --for=condition=available deployment/mongodb --timeout=120s
	@echo "deploying backend pod"
	kubectl apply -f k8s/backend.yml
	kubectl wait --for=condition=available deployment/backend --timeout=120s
	@echo "deploying frontend pod"
	kubectl apply -f k8s/frontend.yml
	kubectl wait --for=condition=available deployment/frontend --timeout=120s
	@echo "deploying doc"
	kubectl apply -f k8s/documentation.yml
	kubectl wait --for=condition=available deployment/documentation --timeout=120s
	@echo "exposing services"
	kubectl get services
	minikube service frontend --url

compose:
	@echo "Composing the project"
	docker compose down -v 
	docker compose up

complete: python-setup npm-setup k8s-setup compose
	@echo "Running complete project"
	@echo "You might wanna run the 'make dotenv' command and fill its values before running this."