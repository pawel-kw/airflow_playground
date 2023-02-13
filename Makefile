.SILENT: ;
AIRFLOW_VERSION=2.2.4
.PHONY: help
help: ## List all described targets available
	@awk -F ':|##' '/^[^\t].+:.*##/ { printf "\033[36m%-28s\033[0m -%s\n", $$1, $$NF }' $(MAKEFILE_LIST) | sort

.sentinels:
	# A place to keep track of make targets that are done
	mkdir -p .sentinels

.PHONY: venv
venv: ## (Experimental) Create a local venv environment at .venv for code completion in IDE
	python3 -m venv .venv
	source .venv/bin/activate && pip install apache-airflow[gcp]==$(AIRFLOW_VERSION) --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-$(AIRFLOW_VERSION)/constraints-`python --version | cut -d " " -f 2 | cut -d "." -f 1-2`.txt"	

.sentinels/venv.sentinel: .sentinels
	@make venv
	touch $@

.PHONY: up
up: ## Start the Airflow tutorial
	docker-compose -f .docker/docker-compose.yaml up

.PHONY: stop
stop: ## Stop the Airflow tutorial
	docker-compose -f .docker/docker-compose.yaml stop

.PHONY: down
down: ## Down the Airflow tutorial
	docker-compose -f .docker/docker-compose.yaml down

.PHONY: restart
restart: ## Restart the Airflow tutorial
	docker-compose -f .docker/docker-compose.yaml restart

.PHONY: password
password: ## Get the password for the local Airflow
	docker-compose -f .docker/docker-compose.yaml exec airflow-webserver cat /opt/airflow/standalone_admin_password.txt