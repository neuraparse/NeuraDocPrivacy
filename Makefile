.PHONY: help install install-dev test test-cov lint format clean build dist install-spacy

# Default target
help:
	@echo "NeuraDocPrivacy - Available commands:"
	@echo ""
	@echo "Installation:"
	@echo "  install      - Install production dependencies"
	@echo "  install-dev  - Install development dependencies"
	@echo "  install-spacy- Install spaCy English model"
	@echo ""
	@echo "Development:"
	@echo "  test         - Run tests"
	@echo "  test-cov     - Run tests with coverage"
	@echo "  lint         - Run linting checks"
	@echo "  format       - Format code with black"
	@echo "  clean        - Clean build artifacts"
	@echo ""
	@echo "Building:"
	@echo "  build        - Build the application"
	@echo "  dist         - Create distribution package"
	@echo ""
	@echo "Running:"
	@echo "  run          - Run the GUI application"
	@echo "  run-cli      - Run the command-line interface"

# Installation
install:
	pip install -r requirements.txt

install-dev:
	pip install -e ".[dev]"
	pre-commit install

install-spacy:
	python -m spacy download en_core_web_sm

# Development
test:
	pytest tests/ -v

test-cov:
	pytest tests/ --cov=. --cov-report=html --cov-report=term-missing

lint:
	flake8 .
	mypy . --ignore-missing-imports

format:
	black .
	isort .

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

# Building
build:
	python -m build

dist: clean build

# Running
run:
	python main.py

run-cli:
	python pdf_masker.py --help

# Docker (if needed)
docker-build:
	docker build -t neura-doc-privacy .

docker-run:
	docker run -it --rm -v $(PWD):/app neura-doc-privacy

# Release
release:
	@echo "Creating release..."
	@read -p "Enter version (e.g., 1.2.0): " version; \
	git tag -a v$$version -m "Release v$$version"; \
	git push origin v$$version

# Setup development environment
setup-dev: install-dev install-spacy
	@echo "Development environment setup complete!"
	@echo "Run 'make run' to start the application"

# Quick check
check: lint test
	@echo "All checks passed!"

# Install all dependencies
all: install install-dev install-spacy
	@echo "All dependencies installed!" 