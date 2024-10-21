.PHONY: help
help:  ## show definitions of all functions
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: lint
lint:  ## run task lint
	ruff check .; ruff check . --diff

.PHONY: format
format:  ## run task format
	ruff check . --fix; ruff format .

.PHONY: install
install:  ## install all production dependencies
	@pip3 install .

.PHONY: install-dev
install-dev:  ## install all dev dependencies
	@pip3 install -e .[dev]

.PHONY: tests
tests:  ## run all tests
	pytest -s -x --cov=fastapi_zero -vv

.PHONY: run
run:  ## Running the application
	uvicorn fastapi_zero.app:app  --proxy-headers --port 5000 --timeout-keep-alive 90 --log-level info --log-config log_conf.yaml

.PHONY: run-dev
run-dev:  ## Running the dev application
	uvicorn fastapi_zero.app:app  --proxy-headers --port 5000 --reload --timeout-keep-alive 90 --log-level info --log-config log_conf.yaml

.PHONY: flake
flake:  ## Apply flake8 checker
	@flake8 .

.PHONY: auto-black
auto-black:  ## Apply black formatter
	@python -m black .
