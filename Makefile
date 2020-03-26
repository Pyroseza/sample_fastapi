.PHONY: help

.DEFAULT_GOAL := help


help: ## This help.
	@echo
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo


build: ## Build developer containers.
	docker-compose build

up: ## Run developer containers.
	docker-compose up

silenceup: ## Run developer containers without print messages.
	docker-compose up -d
