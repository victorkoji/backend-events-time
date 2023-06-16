IMAGE_NAME_API=events_api
IMAGE_NAME_DATABASE=database
DATABASE_USER=postgres
DATABASE_NAME=postgres
DATABASE_PATH_CONFIG=./src/config/database.py

build:
	docker-compose build

up-silent:
	docker compose up -d && \
	make copy-folder-packages

up:
	docker-compose up -d && \
	make copy-folder-packages && \
	docker-compose logs -f web

up-machine:
	pip install -r requirements.txt && \
	cd src/ && \
	python -m flask run --host=0.0.0.0

down:
	docker-compose down

shell:
	docker exec -it $(IMAGE_NAME_API) bash

copy-folder-packages:
	@if [ ! -d ./libs/ ]; then\
		docker cp $(IMAGE_NAME_API):/usr/local/lib/python3.9/site-packages ./libs; \
	fi

db-create-migration:
	docker exec $(IMAGE_NAME_API) orator make:migration $(NAME)

db-migrate:
	docker exec $(IMAGE_NAME_API) orator migrate -f -c $(DATABASE_PATH_CONFIG)

db-migrate-rollback:
	docker exec $(IMAGE_NAME_API) orator migrate:rollback -f -c $(DATABASE_PATH_CONFIG)

db-shell:
	docker exec -it $(IMAGE_NAME_DATABASE) psql -U $(DATABASE_USER) -d $(DATABASE_NAME)
