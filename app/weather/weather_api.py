# import the module
import python_weather

import asyncio
import os

async def getweather(city_name='New York', unit=python_weather.METRIC):
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
    weather = await client.get(location=city_name, unit=unit)

    '''# returns the current day's forecast temperature (int)
    print(f'Temperature: {weather.temperature}')

    # get the weather forecast for a few days
    for daily in weather.daily_forecasts:
      print(f'Daily: {daily}')

      # hourly forecasts
      for hourly in daily.hourly_forecasts:
        print(f' --> {hourly!r}')'''
        
    return weather

'''
  Uses the weather api to return specific information about the weather
'''
def fetch():
  weather = asyncio.run(getweather())
  forecast = {
    "coordinates": weather.coordinates,
    "country": weather.country,
    "datetime": weather.datetime,
    "description": weather.description,
    "feels_like": weather.feels_like,
    "humidity": weather.humidity,
    "kind": weather.kind,
    "local_population": weather.local_population,
    "locale": weather.locale,
    "location": weather.location,
    "precipitation": weather.precipitation,
    "pressure": weather.pressure,
    "region": weather.region,
    "temperature": weather.temperature,
    "ultraviolet": weather.ultraviolet,
    
    "precipitation_unit" : weather.unit.precipitation,
    "pressure_unit": weather.unit.pressure,
    "temperature_unit": weather.unit.temperature,
    "visibility_unit": weather.unit.visibility,
    "velocity_unit" : weather.unit.velocity,
    
    
    "visibility": weather.visibility,
    "wind_direction": weather.wind_direction,
    "wind_speed": weather.wind_speed,
    
    "daily_forecasts": weather.daily_forecasts,
  }
  
  return forecast

if __name__ == '__main__':
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  unit = python_weather.METRIC
  w = asyncio.run(getweather(city_name='Milan', unit=unit))
  
  print(w.unit.pressure)