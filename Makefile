# ================================================================= #
# HELPER
# ================================================================= #

## help: print this help message
.PHONY: help
help:
	@echo 'Usage'
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' | sed -e 's/^/ /'

.PHONY: confirm
confirm:
	@echo -n 'Are you sure? [y/N] ' && read ans && [ $${ans:-N} = y ]


# ================================================================= #
# DEVELOPMENT
# ================================================================= #

## runserver: run the server
.PHONY: runserver
runserver:
	python manage.py runserver 0.0.0.0:8000

## makemigrations: make new migrations
.PHONY: makemigrations
makemigrations:
	python manage.py makemigrations

## migrate: migrate the new migrations to database
.PHONY: migrate
migrate:
	python manage.py migrate