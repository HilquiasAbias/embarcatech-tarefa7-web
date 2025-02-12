from django.urls import path
from .apps import DanielConfig
from . import views
from .api import api

app_name = DanielConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', api.urls),
]
