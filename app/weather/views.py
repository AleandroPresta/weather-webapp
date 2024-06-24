from django.shortcuts import render
from . import weather_api

import logging

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  filename='logs/weather_views.log',
  )

# Create your views here.
def weather_view(request):
    logging.info('Calling weather_view')
    weather = weather_api.getweather()
    logging.debug(f'Weather: {weather!r}')
    logging.info('Redirecting to weather/weather.html')
    return render(request, 'weather/weather.html', {'weather': weather})