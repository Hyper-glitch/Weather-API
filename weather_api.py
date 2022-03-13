from urllib.parse import urljoin
import urllib.parse

import requests


class WeatherApi:
    def __init__(self, language, metric_system):
        self.host = 'https://wttr.in'
        self.params = {f'nTq{metric_system}': '', 'lang': f'{language}', }

    def get_weather(self, city):
        url = WeatherApi.create_url(city=city, host=self.host)
        response = requests.get(url=url, params=self.params)
        response.raise_for_status()
        print(response.text)

    @staticmethod
    def create_url(city, host):
        encoded_city = urllib.parse.quote_plus(city)
        url = urljoin(host, encoded_city)
        return url


if __name__ == '__main__':
    weather_instance = WeatherApi(language='ru', metric_system='m')
    weather_instance.get_weather(city='london')
    weather_instance.get_weather(city='Череповец')
    weather_instance.get_weather(city='аэропорт Шереметьево')
