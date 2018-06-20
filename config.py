from collections import OrderedDict


# Basic:
TELEGRAM_TOKEN = "490322267:AAGLZz4UaTSsUPnxEzMlDxX-jowpTa4qp4o"
ENDPOINTS = OrderedDict(sorted({
    "1) /start": "Welcome message",
    "2) /help": "List of a valid commands for the bot",
    "3) /kurs": "Current exchange rate (USD, EUR, RUR, BTC)",
    "4) /weather": "Today's weather in <city>. 'Lviv' by default",
    "5) /stop_info (BETA)": "Shows information about all vehicles "
                            "that arrive on certain stop"
}.items()))

# PrivatBank:
PRIVAT_BASE_URL = "https://api.privatbank.ua/p24api"

# Weather:
WEATHER_API_KEY = "d9fe844fc29d95d457b1cf5148b34acf"
WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"


# TransportInfo:
TRANSPORT_BASE_URL = "http://82.207.107.126:13541/SimpleRide/LAD/SM.WebApi/api"
ALL_STOPS = "/stops/"
