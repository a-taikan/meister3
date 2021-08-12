from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic import base
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/', views.start),
]