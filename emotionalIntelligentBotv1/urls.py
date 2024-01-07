from django.contrib import admin
from django.urls import path , include
from .views import view_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/",view_app,)
]
