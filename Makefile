.PHONY: help lint validate test

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

lint: ## Lint Markdown files
	npx markdownlint-cli 'profile/**/*.md'

validate: ## Validate required profile assets exist
	node scripts/validate-profile.js

test: lint validate ## Run all checks
