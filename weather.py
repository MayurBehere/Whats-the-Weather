from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()
def get_weather(city ="Pune"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&q={city}&units=metric"

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** GETTING WEATHER DATA ***\n')

    city = input("Enter city name: ")  
    weather_data = get_weather(city)
    pprint('\n')
    pprint(weather_data) 