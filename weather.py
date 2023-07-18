#weather.py

import requests
class Weather:
    def __init__(self, error=0, city_name='',weather_data={}):
        self.error= error
        self.city_name= city_name
        self.weather_data=weather_data


    def get_weather_info(self):
        weather_api_key = "3dc06380d440e4afeac98d7f604cbeb4"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city_name},kor&appid={weather_api_key}"
        self.weather_data = requests.get(url).json()
        # print(self.weather_data)
        return self.weather_data
weather = Weather(city_name='노원구')        
weather.get_weather_info()
