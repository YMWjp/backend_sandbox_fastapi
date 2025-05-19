.PHONY: up down build logs up-d

# Start containers
up:
	docker compose up

# Start containers in detached mode
up-d:
	docker compose up -d

# Stop containers
down:
	docker compose down

# Build images
build:
	docker compose build

# Show logs
logs:
	docker compose logs -f

# Build and run containers
build-up:
	docker compose up --build

# Restart containers
restart: down up-d 