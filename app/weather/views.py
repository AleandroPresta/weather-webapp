from django.shortcuts import render
from . import weather_api

import logging

# Create your views here.
def weather_view(request):
    logging.info('Calling weather_view')
    forecast = weather_api.fetch()
    logging.info('Redirecting to weather/weather.html')
    return render(
        request, 
        'weather/weather.html', 
        {
            'forecast': forecast
        })