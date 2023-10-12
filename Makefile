.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build:	## Build project with compose
	docker-compose build

.PHONY: up
up:	## Run project with compose
	docker-compose up

.PHONY: migrate-apply
migrate-apply: ## apply alembic migrations to database/schema
	docker-compose run --rm app alembic upgrade head

.PHONY: migrate-create
migrate-create:  ## Create new alembic database migration aka database revision.
	docker-compose up -d db | true
	docker-compose run --no-deps app alembic revision --autogenerate -m "$(msg)"

.PHONY: test
test:	## Run project tests
	docker-compose -f docker-compose.yml -f docker-compose.test.yml run --rm app pytest
