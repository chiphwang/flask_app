# -*- coding: utf-8 -*-

import os
import forecastio
from geopy.geocoders import Nominatim


from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
geolocator = Nominatim()
api_key=os.environ['weather_token']


def get_weather(address):
    api_key=os.environ['weather_token']
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
    summary = forecast.summary
    temperature = forecast.temperature
    return "{} and {}° at {}".format(summary, temperature, address)
