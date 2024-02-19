from django.http import HttpRequest
from django.http import HttpResponse
from django.urls import path,include
from django.contrib import admin
from emotionalBot import views
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('emotionalBot.urls',namespace="base")),
    path('login/', views.bot_login, name='login'),
    path('register/', views.bot_register, name='register'),
    path('logout/', views.bot_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('benefits/', views.benefits, name='benefits'),


]