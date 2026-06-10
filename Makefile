.DEFAULT_GOAL := help

.PHONY: help lint lint-fix test validate install clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

install: ## Install dev dependencies
	npm install

lint: ## Lint Markdown files
	npm run lint

lint-fix: ## Auto-fix Markdown lint issues
	npm run lint:fix

test: ## Run tests
	npm test

validate: ## Validate profile assets exist
	npm run validate

clean: ## Remove node_modules
	rm -rf node_modules
