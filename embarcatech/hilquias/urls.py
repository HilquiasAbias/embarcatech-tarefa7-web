from django.urls import path
from .apps import HilquiasConfig
from . import views
from .api import api

app_name = HilquiasConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', api.urls),
]
