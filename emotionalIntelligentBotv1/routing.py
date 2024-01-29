from . import user
from .wsgi import *
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path

import emotionalIntelligentBotv1
from .user import UserConsumer  # user class is created by myself
from .user import UserConsumer

url_patterns_socket = [
    re_path(r'^ws/chat/$', user.UserConsumer.as_asgi()),

]
