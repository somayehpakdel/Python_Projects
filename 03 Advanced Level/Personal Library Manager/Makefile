.PHONY: help up up-backend down build

help: ## Show this help message
    @echo 'Usage: make [TARGET]'
    @echo ''
    @echo 'Targets:'
    @awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

up: ## Run the full stack (backend + frontend)
    @echo "Starting full stack..."
    docker-compose -f docker-compose.yml -f docker-compose.frontend.yml up --build

up-backend: ## Run only the uv backend (api + db)
    @echo "Starting backend only..."
    docker-compose -f docker-compose.yml up --build

down: ## Stop and remove all containers
    @echo "Stopping all services..."
    docker-compose -f docker-compose.yml -f docker-compose.frontend.yml down

build: ## Build all Docker images
    @echo "Building all images..."
    docker-compose -f docker-compose.yml -f docker-compose.frontend.yml build