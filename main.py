import uvicorn
from fastapi import FastAPI
from src.api.endpoints.users import router as user_router
from src.api.endpoints.tasks import router as task_router


app = FastAPI()
app.include_router(router=user_router, prefix='/users')
app.include_router(router=task_router, prefix='/tasks')


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0',
                port=8080, reload=True, workers=1)
