from django.contrib import admin
from django.urls import path, include
from meister import views as meister_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('meister.urls')),
]
