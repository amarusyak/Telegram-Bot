import cherrypy
import config
import telebot


bot = telebot.TeleBot(config.TELEGRAM_TOKEN)


@bot.message_handler(func=lambda message: True, content_types=["text"])
def repeat_all_messages(message):
    bot.reply_to(message, message.text)


class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in (cherrypy.request.headers
                                and 'content-type' in cherrypy.request.headers
                                and cherrypy.request.headers['content-type'] ==
                                    'application/json'):
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)


if __name__ == '__main__':
    bot.remove_webhook()
    with open(config.WEBHOOK_SSL_CERT, 'r') as ssl_cert:
        bot.set_webhook(url=(config.WEBHOOK_URL_BASE + config.WEBHOOK_URL_PATH),
                        certificate=ssl_cert)
    cherrypy.quickstart(WebhookServer(), config.WEBHOOK_URL_PATH, {'/': {}})
    # bot.polling(none_stop=True)
