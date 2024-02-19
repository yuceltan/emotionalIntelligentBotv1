from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

import emotionalBot

from emotionalBot.views import ViewApp
app_name = "chat"

urlpatterns = [path('',ViewApp.as_view(),name='chat_view'),
               path('login/',views.bot_login, name = 'login'),
               path('register/',views.bot_register, name = 'register'),
                path('logout/',views.bot_logout, name = 'logout'),
               path('home/', views.home, name='home'),
               path('benefits/', views.benefits, name='benefits'),
               ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)