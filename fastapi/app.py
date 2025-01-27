from fastapi import FastAPI
from http import HTTPStatus
from fast.schemas import MessageSchema

from fast.routers import users, auth


app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=MessageSchema)
def read_root():
    return {'message': 'hello world'}

