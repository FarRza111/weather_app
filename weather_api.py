import json
from typing import Final
import requests
from model import Weather
from datetime import datetime as dt


API_KEY: Final[str] = '4a7cc3bc3876cf5256f165951ef2a52c'
BASE_URL: Final[str] = 'https://api.openweathermap.org/data/2.5/forecast'

def get_weather(cit_name:str, mock:bool = True)-> dict:
    if mock:
        with open('dummy_data.json') as f:
            return json.load(f)

    payload:dict = {'q': cit_name, 'appid': API_KEY, 'units': 'metric'}
    request = requests.get(url = BASE_URL, params=payload)
    data:dict = request.json()

    # with open('dummy_data.json', 'w') as f:
    #     json.dump(data, f)

    return data

def get_weather_details(weather:dict) -> list[Weather]:
    days: list[dict] = weather.get('list')

    list_of_weather: list[Weather] = []
    for day in days:
        w: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                             details=(details := day.get('main')),
                             temp=details.get('temp'),
                             weather=(weather := day.get('weather')),
                             description=weather[0].get('description'))
        list_of_weather.append(w)
    return list_of_weather


if __name__ == "__main__":
    current_weather: dict = get_weather('tokyo', mock= True)
    weather: list[Weather] = get_weather_details(current_weather)

    for w in weather:
        print(w)




