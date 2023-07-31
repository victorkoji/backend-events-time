IMAGE_NAME_API=events_api
IMAGE_NAME_DATABASE=database
DATABASE_USER=postgres
DATABASE_NAME=postgres
DATABASE_PATH_CONFIG=./src/config/database_config.py
DATABASE_PATH_CONFIG_TEST=./tests/config/database_config.py

.PHONY: build
build:
	docker-compose build --no-cache

.PHONY: up-silent
up-silent:
	docker compose up -d

.PHONY: up
up:
	docker-compose up -d && \
	docker-compose logs -f web

.PHONY: up-machine
up-machine:
	pip install -r requirements.txt && \
	cd src/ && \
	uvicorn app:app --port 5000 --reload

.PHONY: down
down:
	docker-compose down

.PHONY: shell
shell:
	docker exec -it $(IMAGE_NAME_API) bash

.PHONY: copy-folder-packages
copy-folder-packages:
	@if [ ! -d ./libs/ ]; then\
		docker cp $(IMAGE_NAME_API):/usr/local/lib/python3.9/site-packages ./libs; \
	fi

.PHONY: db-create-migration
db-create-migration:
	docker exec $(IMAGE_NAME_API) orator make:migration $(NAME)

.PHONY: db-migrate
db-migrate:
	docker exec $(IMAGE_NAME_API) orator migrate -f -c $(DATABASE_PATH_CONFIG)

.PHONY: db-migrate-rollback
db-migrate-rollback:
	docker exec $(IMAGE_NAME_API) orator migrate:rollback -f -c $(DATABASE_PATH_CONFIG)

.PHONY: db-seed
db-seed:
	docker exec $(IMAGE_NAME_API) orator db:seed -f -c $(DATABASE_PATH_CONFIG)

.PHONY: db-create-seed
db-create-seed:
	docker exec $(IMAGE_NAME_API) make:seed $(NAME)

.PHONY: db-shell
db-shell:
	docker exec -it $(IMAGE_NAME_DATABASE) psql -U $(DATABASE_USER) -d $(DATABASE_NAME)

.PHONY: test
test:
	make db-test-migrate && \
	docker exec -it $(IMAGE_NAME_API) pytest $(TEST_PATH)

.PHONY: test-coverage
test-coverage:
	docker exec -it $(IMAGE_NAME_API) pytest --cov=src/. --cov-report=html

.PHONY: db-test-migrate
db-test-migrate:
	docker exec $(IMAGE_NAME_API) orator migrate -f -c $(DATABASE_PATH_CONFIG_TEST)


.PHONY: lint
lint:
	docker exec $(IMAGE_NAME_API) pylint ./src
