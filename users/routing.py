from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("chat/", consumers.ConnectConsumer.as_asgi()),
    path("chat1/", consumers.ChatConsumer.as_asgi()),
]
