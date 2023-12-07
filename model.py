import datetime
from datetime import datetime as dt
from dataclasses import dataclass

@dataclass
class Weather:
    date:dt
    details:dict
    temp:str
    weather: list[dict]
    description:str

    def __str__(self):
        return f'{self.date} {self.temp}C {self.description}'


# weather_data = {
#     'date': datetime.date(2023, 12, 7),
#     'details': {'location': 'City', 'humidity': 70},
#     'temp': '25',
#     'weather': [{'condition': 'Clear', 'wind_speed': 10}],
#     'description': 'Sunny day'
# }
# 
# weather_instance = Weather(**weather_data)
# print(weather_instance)


