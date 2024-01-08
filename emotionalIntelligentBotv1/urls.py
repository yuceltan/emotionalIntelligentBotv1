from django.http import HttpRequest
from django.http import HttpResponse
from django.urls import path,include
from django.contrib import admin
urlpatterns = [

    path('admin/', admin.site.urls),
    path(r'C:\Users\yucel\Documents\MY PROJECTS\emotionalIntelligentBotv1\emotionalBot', include('emotionalBot.urls')),


]