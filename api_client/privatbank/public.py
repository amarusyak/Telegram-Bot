import config


class BankPublicAPI:
    def __init__(self, client):
        self._client = client
        self._base = config.PRIVAT_BASE_URL

    def get_current_courses(self):
        endpoint = '/pubinfo'
        url = self._base + endpoint
        params = {
            'json': True,
            'exchange': True,
            'coursid': 5
        }
        return self._client.make_call(method='get',
                                      request=url,
                                      params=params)

    @staticmethod
    def serialize_response(response):
        base_str = ("{currency}\n"
                    "    Buy: {buy} {base_ccy}\n"
                    "    Sale: {sale} {base_ccy}\n\n")
        return ''.join([base_str.format(currency=item['ccy'],
                                        buy=item['buy'],
                                        sale=item['sale'],
                                        base_ccy='UAH' if item['ccy'] != 'BTC'
                                            else 'USD')
                        for item in response])
