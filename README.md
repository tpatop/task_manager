# (FastAPI) Realtime Task Manager

## Features:
* User registration and authentication (OAuth2 + JWT)
* Alembic database migrations
  
## Getting started
1. Clone this repository and go to folder
```
git clone git@github.com:tpatop/task_manager.git
cd task_manager
```
2. Install Python 3.11 and Docker-compose
3. Create a virtual environment
```
python3.11 -m vevn <python_core_dir>
```
4. Install requirements
```
source <python_core_dir>/bin/activate
python3.11 -r requirements.txt
```
5. Create a .env file and fill it in according to the sample file .env.example
## Usage
### Running Database Server with Adminer
```
docker-compose up
```
Wait for successful launch
### Running API
```
<python_core_dir>/bin/python <dir task_manager>/app/main.py
```

## Documentation
http://127.0.0.1:8080/docs
