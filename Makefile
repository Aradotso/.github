.PHONY: install lint format format-write help

help:
	@echo "Available commands:"
	@echo "  make install      Install development dependencies"
	@echo "  make lint         Run markdown linting"
	@echo "  make format       Verify formatting with prettier"
	@echo "  make format-write Fix formatting issues with prettier"

install:
	npm install

lint:
	npm run lint

format:
	npm run format

format-write:
	npm run format:write
