import pytest

from references.models import Room


@pytest.mark.django_db
def test_create_room(auth_client):
    payload = dict(title='test room')
    response = auth_client.post('/references/rooms/', payload)
    room = Room.objects.get(title=payload['title'])
    assert room.title == response.data['title']


@pytest.mark.django_db
def test_get_room_detail(auth_client):
    response = auth_client.get('/references/rooms/0/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_room(auth_client, room):
    payload = dict(title='updated testroom')
    response = auth_client.patch(f'/references/rooms/{room.id}/', payload)
    room.refresh_from_db()
    assert room.id == response.data['id']
    assert room.title == payload['title']


@pytest.mark.django_db
def test_delete_room(auth_client, room):
    # payload = dict(title='updated testroom')
    response = auth_client.delete(f'/references/rooms/{room.id}/')
    assert response.status_code == 204
    with pytest.raises(Room.DoesNotExist):
        room.refresh_from_db()
