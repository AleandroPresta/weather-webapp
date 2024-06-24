# import the module
import python_weather

import asyncio
import os

import logging
logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  filename='logs/weather_api.log',
  )

async def getweather(city_name='New York', unit=python_weather.METRIC):
  logging.info(f'Calling getweather with\ncity_name={city_name}\nunit={unit}')
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
    weather = await client.get(location=city_name, unit=unit)
    logging.debug(f'Weather: {weather!r}')

    '''# returns the current day's forecast temperature (int)
    print(f'Temperature: {weather.temperature}')

    # get the weather forecast for a few days
    for daily in weather.daily_forecasts:
      print(f'Daily: {daily}')

      # hourly forecasts
      for hourly in daily.hourly_forecasts:
        print(f' --> {hourly!r}')'''
        
    return weather

if __name__ == '__main__':
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  input_city = input("Enter the city name: ")
  unit = python_weather.METRIC
  w = asyncio.run(getweather(city_name=input_city, unit=unit))
  print(w)