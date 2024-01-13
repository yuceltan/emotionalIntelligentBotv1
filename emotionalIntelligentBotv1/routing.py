from django.urls import re_path
from . import user #user class is created by myself

url_patterns_socket = [
    re_path(r"ws/emotionalIntelligentBotv1/$",user.UserConsumer.as_asgi()),
]

