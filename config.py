from collections import OrderedDict
from yaml import load


with open("tokens.yaml", 'r') as yaml_file:
    _tokens = load(yaml_file)['tokens']


# Basic:
TELEGRAM_TOKEN = _tokens['telegram']
ENDPOINTS = OrderedDict(sorted({
    "1) /start": "Welcome message",
    "2) /help": "List of a valid commands for this bot",
    "3) /kurs": "Current exchange rate (USD, EUR, RUR, BTC)",
    "4) /weather": "Today's weather in <city>. 'Lviv' by default",
    "5) /stopinfo": "Shows information about all vehicles that will "
                    "arrive on certain stop"
}.items()))

# PrivatBank:
PRIVAT_BASE_URL = "https://api.privatbank.ua/p24api"

# Weather:
WEATHER_API_KEY = _tokens['weather']
WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

# TransportInfo:
TRANSPORT_BASE_URL = "http://82.207.107.126:13541/SimpleRide/LAD/SM.WebApi/api"
ALL_STOPS_ENDPOINT = "/stops/"
