from django.shortcuts import render
from . import weather_api

import logging
from .logging_config import configure_logging

configure_logging()

logger = logging.getLogger(__name__)

# Create your views here.
def weather_view(request):
    logging.info('Calling weather_view')
    weather = weather_api.getweather()
    logging.debug(f'Weather: {weather!r}')
    logging.info('Redirecting to weather/weather.html')
    return render(request, 'weather/weather.html', {'weather': weather})