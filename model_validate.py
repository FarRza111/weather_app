from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Weather:
    # date: datetime
    details: dict
    temp: str
    weather: List[dict]
    description: str

    def __post_init__(self):

        if not isinstance(self.details, dict):
            raise ValueError("Invalid 'details' attribute. Must be a dictionary.")

        if not isinstance(self.temp, str):
            raise ValueError("Invalid 'temp' attribute. Must be a string.")

        if not isinstance(self.weather, list):
            raise ValueError("Invalid 'weather' attribute. Must be a list.")

        if not isinstance(self.description, str):
            raise ValueError("Invalid 'description' attribute. Must be a string.")

    def __str__(self):
        return f'{self.temp}C {self.description}'

weather_data = {
    # 'date': datetime.date(2023, 12, 7),
    'details': {'location': 'City', 'humidity': 70},
    'temp': '25',
    'weather': [{'condition': 'Clear', 'wind_speed': 10}],
    'description': 'Sunny day'
}


weather_instance = Weather(**weather_data)
print(weather_instance)
