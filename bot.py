import config
import telebot

from api_client.client import Client
from api_client.open_weather_map.public import WeatherPublicAPI
from api_client.privatbank.public import BankPublicAPI
from api_client.transport_info.public import TransportInfoAPI
from logger.logger import log

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
api_client = Client()


# Handle '/start'
@bot.message_handler(commands=['start'])
@log
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Hi there! I am a simple bot that is going to help you "
                     "with some trivial, but really helpful tasks :)\n"
                     "Please, send '/help' to get a list of a valid commands.")


# Handle '/help'
@bot.message_handler(commands=['help'])
@log
def send_instructions(message):
    bot.send_message(message.chat.id, '\n'.join(
        [key + ': ' + config.ENDPOINTS[key] for key in config.ENDPOINTS]))


# Handle '/kurs'
@bot.message_handler(commands=['kurs'])
@log
def show_exchange_rate(message):
    privatbank_api = BankPublicAPI(api_client)
    response = privatbank_api.get_current_courses()
    bot.reply_to(message, "(c) Privat Bank\n\n" +
                 privatbank_api.serialize_response(response))


# Handle '/weather'
@log
@bot.message_handler(commands=['weather'])
def show_weather(message):
    """
    Message example - "/weather in <city>"
    """
    city = message.text[12:]
    if not city:
        city = 'Lviv'

    with open("data/city_list.txt", 'r') as city_list:
        all_cities = city_list.read().split()

    if city.title() not in all_cities:
        bot.reply_to(message, "Incorrect city name - '{}'!".format(city))
    else:
        weather_api = WeatherPublicAPI(api_client)
        response = weather_api.get_todays_weather(city)
        bot.reply_to(message, weather_api.serialize_response(response))


# Handle '/stopinfo'
@bot.message_handler(commands=['stopinfo'])
@log
def show_exchange_rate(message):
    stop = message.text[10:]
    if not stop:
        bot.reply_to(message, "Warning: Enter stop code!")
    elif not stop.isdigit() or len(stop) > 4:
        bot.reply_to(message, "Incorrect stop code - '{}'".format(stop))
    else:
        t_info = TransportInfoAPI(api_client)
        u_stop = t_info.unify_stop_code(stop) if len(stop) is not 4 else stop
        response = t_info.get_stop_info(u_stop)
        bot.reply_to(message, t_info.serialize_response(response))


# Handle all other messages
@bot.message_handler(func=lambda message: True, content_types=['text'])
@log
def echo_message(message):
    bot.reply_to(message, "Incorrect command. "
                          "Use '/help' to list a valid commands for this bot.")


if __name__ == '__main__':
    bot.polling(none_stop=True)
