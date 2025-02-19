from django.urls import path

from water.apps import WaterConfig
from water.views import home

app_name = WaterConfig.name

urlpatterns = [
    path('', home, name='home'),

]