# (FastAPI) Realtime Task Manager

## Features:
* User registration and authentication (OAuth2 + JWT)
* PostgreSQL as a project database
* Adminer for database administration
* Alembic database migrations
* Running in docker containers

## Getting started
1. Clone this repository and go to folder
```
git clone git@github.com:tpatop/task_manager.git
cd task_manager
```
1. Install Docker and Docker-compose
2. Create a .env file and fill it in according to the sample file .env.example
(You can use all the variables from the .env.example file without changes, to do this, create a copy of this file and rename it to .env)

## Usage
### Running the API on the local machine
```
docker-compose up
```

## Documentation
* API - http://localhost:8080/docs
* Adminer - http://localhost:8888