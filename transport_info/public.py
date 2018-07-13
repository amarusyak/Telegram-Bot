import json

from requests import get

import config


class TransportInfoAPI(object):
    def __init__(self):
        self._url = config.TRANSPORT_BASE_URL + config.ALL_STOPS_ENDPOINT

    def get_stop_info(self, stop_code):
        params = {'code': stop_code}
        response = get(self._url, params)
        response.raise_for_status()
        return json.loads(response.json())

    def serialize_response(self, response):
        normalized_data = list()
        for item in response:
            route_name = item.get('RouteName')
            time_to_wait = self.int_seconds_to_str_time(item.get('TimeToPoint'))
            normalized_item = {
                "Route name": repr(route_name),
                "Time to wait": time_to_wait
            }
            normalized_data.append(normalized_item)

        return '\n'.join(
            [item.get("Route name") + ' -> ' + item.get("Time to wait")
             for item in normalized_data]
        ) if normalized_data else "No data found..."

    @staticmethod
    def int_seconds_to_str_time(sec):
        return str(int(sec / 60)) + ' m, ' + str(sec % 60) + ' s'

    @staticmethod
    def unify_stop_code(stop_code):
        return '0' * (4 - len(stop_code)) + stop_code
