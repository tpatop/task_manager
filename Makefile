DC = docker-compose
PROD_COMPOSE = -f prod.docker-compose.yml
DEV_COMPOSE = -f dev.docker-compose.yml

.PHONY: app app-rebuild dev dev-rebuild migrate stop delete

app: ## up production version
	$(DC) $(PROD_COMPOSE) up

app-rebuild: ## up production version with container rebuild
	$(DC) $(PROD_COMPOSE) up --build

dev: ## up development version
	$(DC) $(DEV_COMPOSE) up

dev-rebuild: ## development version with container rebuild
	$(DC) $(DEV_COMPOSE) up --build

migrate: ## alembic migration
	docker exec web alembic upgrade head

stop: ## stop all containers
	docker stop $$(docker ps -a -q) || true

delete: ## delete all containers/images
	docker system prune -a --volumes