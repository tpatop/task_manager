import uvicorn
from fastapi import FastAPI
from api.endopoints.users import router as user_router
from db.session import init_db, close_db

app = FastAPI()
app.include_router(router=user_router, prefix='/users')


@app.on_event('startup')
async def on_startup():
    await init_db()


@app.on_event('shutdown')
async def shutdown():
    await close_db()


@app.get('/')
async def root():
    return {'message': 'Root'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1',
                port=8080, reload=True, workers=1)
