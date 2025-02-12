from django.urls import path
from .apps import MatheusConfig
from . import views
from .api import api

app_name = MatheusConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', api.urls),
]
