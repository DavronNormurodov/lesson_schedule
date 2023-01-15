import pytest


@pytest.mark.django_db
def test_register_user(client):
    payload = {
        "username": "testuser1",
        "password": "1234",
        "first_name": "string",
        "last_name": "string",
        "email": "test@gmail.com",
        "role": None
    }
    response = client.post('/users/register/', payload)
    data = response.data
    assert data['first_name'] == payload['first_name']
    assert data['username'] == payload['username']
    assert data['last_name'] == payload['last_name']
    assert data['email'] == payload['email']


@pytest.mark.django_db
def test_login_user(user, client):
    # payload = {
    #     "username": "testuser1",
    #     "password": "1234",
    #     "first_name": "string",
    #     "last_name": "string",
    #     "email": "test@gmail.com",
    #     "role": None
    # }
    # client.post('/users/register/', payload)
    response = client.post('/users/login/', {"username": "testuser2", "password": "1234"})
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_me(user, auth_client):
    # log_res = client.post('/users/login/', {"username": "testuser2", "password": "1234"})
    # client.credentials(HTTP_AUTHORIZATION='Bearer ' + log_res.data['access'])
    response = auth_client.get('/users/users/get_me/')
    assert response.status_code == 200
    data = response.data
    assert data['id'] == user.id
