from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from . import user #user class is created by myself



url_patterns_socket = [
    re_path(r"/emotionalIntelligentBotv1/routing",user.UserConsumer.as_asgi()),
]


application = ProtocolTypeRouter({
    "websocket": URLRouter(
        url_patterns_socket,
    ),
})