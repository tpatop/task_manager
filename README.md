# FastAPI Real-time Task Manager

[English](#english) | [Русский](#русский)

## English
## Features:
* User registration and authentication (OAuth2 + JWT)
* PostgreSQL as a project database
* Adminer for database administration
* Alembic database migrations
* Docker containers for easy deployment

## Getting started
1. Clone this Repository:
```
git clone git@github.com:tpatop/task_manager.git
cd task_manager
```
2. Install Dependencies:
   * Install Docker and Docker-compose
3. Configure Environment Variables:
   * Create a `.env` file and populate it using the provided `.env.example` as a template. You can use the variables from the example without changes or create a copy and rename it to `.env`.
```
cp .env.example .env
```

## Usage
### Running the API Locally for production:
```
make app
```

### Running the API Locally for development:
```
make dev
```

## Documentation
* API - http://localhost:8080/docs
* Adminer - http://localhost:8888

## Additional Information

* Database Migrations:
  * Alembic is used for managing database migrations. If you make changes to the database models, run the following command to apply the migrations:
```
make migrate
```

* Stopping the Services:
    * To stop the services, use the following command:

```
make stop
```

* Rebuilding Images:
    * If you make changes to the Dockerfile or dependencies, rebuild the images with:
```
make app-rebuild
```
or
```
make dev-rebuild
```

* Contributing

You can contribute by opening issues or creating pull requests.


## Русский
## Особенности:
* Регистрация и аутентификация пользователей (OAuth2 + JWT)
* PostgreSQL в качестве базы данных проекта
* Adminer для администрирования базы данных
* Миграции базы данных с использованием Alembic
* Использование Docker-контейнеров для удобного развертывания

## Начало работы:
1. Клонировать данный репозиторий:
```
git clone git@github.com:tpatop/task_manager.git
cd task_manager
```
2. Установить зависимости:
   * Установите Docker и Docker-compose
3. Настройка переменных окружения:
   * Создайте файл .env и заполните его, используя предоставленный .env.example в качестве шаблона. Можно использовать переменные из примера без изменений, либо создать копию и переименовать ее в .env:
```
cp .env.example .env
```

## Использование:
### Запуск API локально для использования
```
make app
```
### Запуск API локально для разработки
```
make app
```

## Документация
* API - http://localhost:8080/docs
* Adminer - http://localhost:8888

## Дополнительная информация:
* Миграции базы данных:
  * Используется Alembic для управления миграциями базы данных. Если внесены изменения в модели базы данных, выполните следующую команду для применения миграций:
```
make migrate
```

* Остановка сервисов:
  * Для остановки сервисов используйте следующую команду:
```
make stop
```

* Пересборка образов:
  * Если внесены изменения в Dockerfile или зависимости, пересоберите образы с помощью:
```
make app-rebuild
```
или
```
make dev-rebuild
```

* Внести свой вклад в разработку:

Вы можете вносить свой вклад, открывая вопросы или создавая pull-запросы.