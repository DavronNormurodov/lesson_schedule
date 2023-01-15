"""
ASGI config for base project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import django
from channels.routing import ProtocolTypeRouter, URLRouter
application = get_asgi_application()
django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')

# from users.middlewares import WebSocketJWTAuthMiddleware
from users import routing

application = ProtocolTypeRouter({
    "http": application,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )
        )
    ),
})
