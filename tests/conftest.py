import pytest
from rest_framework.test import APIClient

from references.models import Room
from users.models.user import User


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    user = User.objects.create_user("testuser2", "1234", first_name="string",
                                    last_name="string", email="test@gmail.com")
    return user


@pytest.fixture
def auth_client(user, client):
    log_res = client.post('/users/login/', {"username": "testuser2", "password": "1234"})
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + log_res.data['access'])
    return client


@pytest.fixture
def room():
    room = Room.objects.create(title="testroom")
    return room
