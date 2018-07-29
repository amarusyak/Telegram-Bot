import requests
import config
import curlify

from logger.logger import Logger

requests.packages.urllib3.disable_warnings()


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

    def post(self, url, headers, params):
        return self._session.post(url=url,
                                  verify=False,
                                  headers=headers,
                                  data=params)

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
    def make_call(self, method, request, params,
                  headers=config.DEFAULT_REQUEST_HEADERS):
        http_method = getattr(self, method)
        headers.update(headers if headers else None)
        response = http_method(url=request, headers=headers, params=params)

        try:
            response.raise_for_status()
        except requests.RequestException as e:
            logger = Logger()
            logger.log('\n'.join([
                "Details:",
                "Request: " + curlify.to_curl(response.request),
                "Response status: " + str(response.status_code),
                "Response: " + response.text,
                "Python Exception: " + str(e) + '\n'
            ]))

        return response.json()
