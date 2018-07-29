import config


class WeatherPublicAPI:
    def __init__(self, client):
        self._client = client
        self._key = config.WEATHER_API_KEY

    def get_todays_weather(self, city):
        params = {
            'q': city,
            'appid': self._key
        }
        return self._client.make_call(method='get',
                                      request=config.WEATHER_BASE_URL,
                                      params=params)

    @staticmethod
    def serialize_response(response):
        applicable_data = response['list'][:3]
        base_str = ("{datetime}\n"
                    "    {weather}\n"
                    "    Temperature: {temp}\n"
                    "    Pressure: {p}\n\n")

        return ''.join([base_str.format(
            datetime=item['dt_txt'],
            weather=item['weather'][0]['description'].capitalize(),
            temp=str(int(round(item['main']['temp'] - 273))) +
                u' \xb0C'.encode('utf-8'),
            p=str(item['main']['pressure']) + ' Pa')
                for item in applicable_data]
        )
