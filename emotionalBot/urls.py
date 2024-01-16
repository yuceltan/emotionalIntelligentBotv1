from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import emotionalBot
from emotionalBot import views
from emotionalBot.views import ViewApp
app_name = "chat"

urlpatterns = [path('',ViewApp.as_view(),name='chat_view')]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)