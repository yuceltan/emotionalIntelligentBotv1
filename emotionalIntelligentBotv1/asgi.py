"""
ASGI config for emotionalIntelligentBotv1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from decouple import config
from channels.routing import get_default_application


import emotionalIntelligentBotv1.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE','emotionalIntelligentBotv1.settings')

django.setup()
application = ProtocolTypeRouter(
    {

        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(emotionalIntelligentBotv1.routing.url_patterns_socket))
                                                 ),
    }
)
