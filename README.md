# FastAPI Real-time Task Manager

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
### Running the API Locally:
```
docker-compose up
```

## Documentation
* API - http://localhost:8080/docs
* Adminer - http://localhost:8888

## Additional Information

* Database Migrations:
    * Alembic is used for managing database migrations. If you make changes to the database models, run the following command to apply the migrations:
```
docker-compose exec web alembic upgrade head
```

* Stopping the Services:
    * To stop the services, use the following command:

```
docker-compose down
```

* Rebuilding Images:
    * If you make changes to the Dockerfile or dependencies, rebuild the images with:
```
docker-compose up --build
```

* Contributing

You can contribute by opening issues or creating pull requests.
