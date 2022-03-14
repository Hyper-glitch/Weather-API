import urllib.parse as urllib

import requests


class WeatherApi:
    def __init__(self, language, measure_system):
        self.host = 'https://wttr.in'
        self.params = {f'nTq{measure_system}': '', 'lang': f'{language}', }

    def get_weather(self, location):
        url = WeatherApi.create_url(location=location, host=self.host)
        response = requests.get(url=url, params=self.params)
        response.raise_for_status()
        return response.text

    @staticmethod
    def create_url(location, host):
        return urllib.urljoin(host, urllib.quote_plus(location))


if __name__ == '__main__':
    weather_instance = WeatherApi(language='ru', measure_system='m')
    locations = ['london', 'Череповец', 'аэропорт Шереметьево']

    for location in locations:
        weather = weather_instance.get_weather(location=location)
        print(weather)
