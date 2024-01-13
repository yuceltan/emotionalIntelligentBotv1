from django.contrib import admin
from django.urls import path

import emotionalBot
from emotionalBot import views
from emotionalBot.views import ViewApp
app_name = "chat"


"""urlpatterns = [
    path('',views.ViewApp),
]"""

urlpatterns = [path('',ViewApp.as_view(),name='chat_view')]