from django.urls import path
from .apps import GustavoConfig
from . import views
from .api import api

app_name = GustavoConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', api.urls),
]
