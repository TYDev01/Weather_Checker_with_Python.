import requests
from dotenv import load_dotenv
import os
from pprint import pprint
from ascii_logo import logo
load_dotenv()


def get_weather_info():
    print(logo)
    print("**** Current weather Info in your area ***")
    city = input("Enter a City name:\n")  # Add any city name

    request_url = (f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&'
                   f'units=imperial')
    # print(request_url)

    weather_data = requests.get(request_url).json()
    # pprint(weather_data)  Un-comment to view the JSON file format
    # So the double pp in "pprint()" is an imported module
    # it's to change the display of the returned JSON file in a more readable format.

    print(f"\n Current weather Info for {weather_data['name']}\n")
    print(f"The weather feels like {weather_data['main']['feels_like']}")
    print(f"The weather temperature is: {weather_data['main']['temp']}")
    print(f'Weather condition will be: {weather_data["weather"][0]["main"]} and'
          f' {weather_data["weather"][0]["description"]}')


if __name__ == "__main__":
    get_weather_info()
