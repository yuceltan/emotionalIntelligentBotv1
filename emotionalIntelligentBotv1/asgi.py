"""
ASGI config for emotionalIntelligentBotv1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from emotionalIntelligentBotv1.routing import application


import emotionalIntelligentBotv1

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emotionalIntelligentBotv1.settings')

django_application = get_asgi_application()
websocket_urlpatterns = emotionalIntelligentBotv1.routing.url_patterns_socket
application = ProtocolTypeRouter(
    {

        "http": application,
        "websocket": AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
                                                 ),
    }
)
