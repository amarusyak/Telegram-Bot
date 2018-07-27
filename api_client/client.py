import requests

from logger.logger import Logger


class Client:
    def __init__(self):
        self._session = requests.Session()

    ######################
    # Basic HTTP methods #
    ######################
    def get(self, url, headers, params):
        return self._session.get(url=url,
                                 verify=False,
                                 headers=headers,
                                 params=params)

    def post(self, url, headers, data):
        return self._session.post(url=url,
                                  verify=False,
                                  headers=headers,
                                  data=data)

    def put(self, url, headers, params):
        return self._session.put(url=url,
                                 verify=False,
                                 headers=headers,
                                 params=params)

    def delete(self, url, headers, params):
        return self._session.put(url=url,
                                 verify=False,
                                 headers=headers,
                                 params=params)

    # Unified HTTP call method
    def make_call(self, method, request, params):
        http_method = getattr(self, method)
        response = http_method(request, params)

        try:
            response.raise_for_status()
        except requests.RequestException as e:
            logger = Logger()
            logger.log(http_method)
            logger.log(e)

        return response.json()
