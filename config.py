import cherrypy


SERVER_IP = "172.17.0.2"

TELEGRAM_TOKEN = "490322267:AAGLZz4UaTSsUPnxEzMlDxX-jowpTa4qp4o"

# PrivatBank:
PRIVAT_BASE_URL = "https://api.privatbank.ua/p24api"

# Server:
WEBHOOK_SSL_CERT = "server/certs/webhook_cert.pem"
WEBHOOK_SSL_PRIV = "server/certs/webhook_pkey.pem"
WEBHOOK_PORT = 443
WEBHOOK_LISTEN = '0.0.0.0'
WEBHOOK_URL_BASE = "https://{ip}:{port}".format(ip=SERVER_IP, port=WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{t}/".format(t=TELEGRAM_TOKEN)

cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})
