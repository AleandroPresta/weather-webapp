from django.shortcuts import render
from . import weather_api
from icecream import ic

import logging

# Create your views here.
def weather_view(request):
    logging.info('Calling weather_view')
    forecast = weather_api.fetch()
    daily_forecasts = extract_daily_forecasts(forecast['daily_forecasts'])
    today_hourly_forecasts = extract_hourly_forecasts(daily_forecasts[0]['hourly_forecasts']) # daily_forecasts[0] is today's forecast
    ic(daily_forecasts)
    logging.info('Redirecting to weather/weather.html')
    return render(
        request, 
        'weather/weather.html', 
        {
            'forecast': forecast,
            'daily_forecasts': daily_forecasts,
            'today_hourly_forecasts': today_hourly_forecasts,
        })
    
    
'''
    Extracts the daily forecasts as list of dictionaries from the generator
'''
def extract_daily_forecasts(daily_forecasts):
    result = [
        {
            'date': daily_forecast.date.strftime('%d-%m'),
            'lowest_temperature': daily_forecast.lowest_temperature,
            'highest_temperature': daily_forecast.highest_temperature,
            'sunrise': daily_forecast.sunrise.strftime('%H:%M'),
            'sunset': daily_forecast.sunset.strftime('%H:%M'),
            'temperature_unit': daily_forecast.unit.temperature, 
        } 
        for daily_forecast in daily_forecasts]

    
    return result


def extract_hourly_forecasts(daily_forecast):
    pass