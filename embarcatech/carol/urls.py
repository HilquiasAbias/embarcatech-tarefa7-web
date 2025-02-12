from django.urls import path
from .apps import CarolConfig
from . import views
from .api import api

app_name = CarolConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', api.urls),
]
