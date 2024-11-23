import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
#requests_url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}&units=metric'


def getCurrentWeather(city = "Ohio"):

    requests_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(requests_url)

    weather_data = requests.get(requests_url, verify=False).json()

    # print(f'\nCurrent Weather for {weather_data["name"]}')
    # print(f'\nCurrent Temp is {weather_data["main"]["temp"]}')
    # print(f'\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.')
    # print("\n\n")

    return weather_data


# if __name__ == "__main__":
#     print('\n Current Weather Condition\n')
#     city = 'Cleveland'
#     weather_data = getCurrentWeather()

#     pprint(weather_data)