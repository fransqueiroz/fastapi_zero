from jwt import decode
from http import HTTPStatus

from fastapi_zero.security import settings, create_access_token


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)
    decoded = decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    assert decoded['test'] == data['test']
    assert decoded['exp']

def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}