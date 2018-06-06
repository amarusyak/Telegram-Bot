from requests import get
import config


class PublicAPI(object):
    def __init__(self):
        self.base = config.PRIVAT_BASE_URL

    def get_current_courses(self):
        endpoint = '/pubinfo'
        url = self.base + endpoint
        params = {
            'json': True,
            'exchange': True,
            'coursid': 5
        }
        response = get(url, params)
        response.raise_for_status()
        return response.json()
