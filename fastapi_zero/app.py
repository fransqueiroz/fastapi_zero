import logging
from http import HTTPStatus

from fastapi import FastAPI

from fastapi_zero.routers import auth, todos, users
from fastapi_zero.schemas import Message

app = FastAPI()
logger = logging.getLogger(__name__)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    logging.error('Teste De Logging')
    return {'message': 'Olá Mundo!'}


# Criando Rotas CRUD para Gerenciamento de Tarefas em FastAPI
