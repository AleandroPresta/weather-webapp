from django.shortcuts import render
from . import weather_api
from icecream import ic

import logging

# Create your views here.
def weather_view(request):
    logging.info('Calling weather_view')
    forecast = weather_api.fetch()
    daily_forecasts = extract_daily_forecasts(forecast['daily_forecasts'])
    logging.debug(f'Daily Forecasts: {daily_forecasts}')
    today_hourly_forecasts = extract_hourly_forecasts(daily_forecasts[0]['hourly_forecasts']) # daily_forecasts[0] is today's forecast
    ic(daily_forecasts[0]['hourly_forecasts'])
    ic(today_hourly_forecasts)
    
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
            'hourly_forecasts': daily_forecast.hourly_forecasts,
        } 
        for daily_forecast in daily_forecasts]

    
    return result


def extract_hourly_forecasts(hourly_forecasts):
    result = [
        {
            'kind': hourly_forecast.kind,
            'humidity': hourly_forecast.humidity,
            'precipitation': hourly_forecast.precipitation,
            'temperature': hourly_forecast.temperature,
            'pressure': hourly_forecast.pressure,
            'time': hourly_forecast.time.strftime('%H:%M'),
            'chances_of_rain': hourly_forecast.chances_of_rain,
            'wind_speed': hourly_forecast.wind_speed,
            'wind_direction': hourly_forecast.wind_direction,
            'visibility': hourly_forecast.visibility,
            'temperature_unit': hourly_forecast.unit.temperature,
            'pressure_unit': hourly_forecast.unit.pressure,
            'velocity_unit': hourly_forecast.unit.velocity,
            'visibility_unit': hourly_forecast.unit.visibility,
            'precipitation_unit': hourly_forecast.unit.precipitation,
            
        }
        for hourly_forecast in hourly_forecasts
    ]
    
    return result