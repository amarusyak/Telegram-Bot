import json

from requests import get

import config


class TransportInfoAPI(object):
    @staticmethod
    def get_stop_info(stop_code):
        url = config.TRANSPORT_BASE_URL + config.ALL_STOPS
        params = {'code': stop_code}
        response = get(url, params)
        response.raise_for_status()
        return json.loads(response.json())

    def serialize_response(self, response):
        normalized_data = list()
        for item in response:
            name = item.get('RouteName')
            time_to = self.int_secs_to_time(item.get('TimeToPoint'))
            normalized_item = {
                "Rout name": repr(name),
                "Time to wait": str(time_to)
            }
            normalized_data.append(normalized_item)

        return '\n\n'.join(
            ["Rout name: " + item.get("Rout name") + '\n' +
             "Time to wait: " + item.get("Time to wait")
             for item in normalized_data]
        ) if normalized_data else "No data was found..."

    @staticmethod
    def int_secs_to_time(sec):
        return str(int(sec / 60)) + ' m, ' + str(sec % 60) + ' s'
