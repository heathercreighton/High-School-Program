"""
title: json_exercise
author: eam3kzn
date: 6/15/18 2:49 PM
"""

import config
import requests
import json

weather = config.weather_api_key
command = "http://api.openweathermap.org/data/2.5/weather?q=Austin,us&units=imperial&APPID=" + weather
response = requests.get(command)

print(json.dumps(response.json(), indent=4))

austin_data = response.json()
print(f"""Temperature: {austin_data['main']['temp']} F
Humidity: {austin_data['main']['humidity']}%""")
