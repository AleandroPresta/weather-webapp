from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.weather_view, name='weather'),
    path('search/<slug:slug>', views.search_weather_view, name='search-weather'),
]
