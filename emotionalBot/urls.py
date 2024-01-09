from django.contrib import admin
from django.urls import path

import emotionalBot
from emotionalBot import views
from emotionalBot.views import view_app

urlpatterns = [
    path('',views.view_app),
]