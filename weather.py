#import modules
import numpy as np
import pandas as pd
import json
import requests
from pprint import pprint

#Enter API key
API_Key = "632bb734697ece7393e3332e16a2788f"

#user input city name
city_name = input("Enter city name: ")

#base_url variable
base_url= "http://api.openweathermap.org/data/2.5/weather?"


#final_url
final_url = base_url + "appid=" + API_Key + "&q=" + city_name

weather_data = requests.get(final_url).json()

pprint(weather_data)