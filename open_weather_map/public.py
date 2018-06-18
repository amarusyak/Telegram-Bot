from requests import get
import config


class WeatherPublicAPI(object):
    @staticmethod
    def get_todays_weather(city):
        params = {
            'q': city,
            'appid': config.WEATHER_API_KEY
        }
        response = get(config.WEATHER_BASE_URL, params)
        response.raise_for_status()
        return response.json()

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
            temp=str(int(round(item['main']['temp'] - 273))),
            p=str(item['main']['pressure']))
                for item in applicable_data]
        )