import os

from users.middlewares import WebSocketJWTAuthMiddleware
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from users import routing

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")

print('asgi ======== ')
application = ProtocolTypeRouter({
    'websocket': WebSocketJWTAuthMiddleware(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
}
)
# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         "websocket": WebSocketJWTAuthMiddleware(URLRouter(routing.websocket_urlpatterns)),
#     }
# )
