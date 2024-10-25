from http import HTTPStatus

from fastapi_zero.schemas import UserPublic
from fastapi_zero.security import create_access_token


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_get_token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token
