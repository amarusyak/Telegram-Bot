import json
import config
import telebot

from privatbank.public import PublicAPI


bot = telebot.TeleBot(config.TELEGRAM_TOKEN)


# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Hi there, I am a simple bot that is going to help you "
                     "with some trivial tasks. Please, send '/help' to get "
                     "a list of a valid commands.")


# Handle '/help'
@bot.message_handler(commands=['help'])
def send_instructions(message):
    bot.send_message(message.chat.id, json.dumps(config.ENDPOINTS))


# Handle '/kurs'
@bot.message_handler(commands=['kurs'])
def show_exchange_rate(message):
    privatbank_api = PublicAPI()
    response = privatbank_api.get_current_courses()
    bot.reply_to(message, privatbank_api.serialize_response(response))


if __name__ == '__main__':
    bot.polling(none_stop=True)
