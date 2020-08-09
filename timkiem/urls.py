from django.urls import path, re_path

from home.views import main
from timkiem.views import timkiem

app_name = 'timkiem'
urlpatterns = [
    path('',timkiem,name="tim-kiem"),
]