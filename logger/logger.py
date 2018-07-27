import config
from datetime import datetime
from os import path, makedirs


def log(funk):
    def inner(*args, **kwargs):
        logger = Logger()
        funk_name = funk.__name__
        logger.log(funk_name)
        funk(*args, **kwargs)
    return inner


class Logger:
    def __init__(self):
        if not path.exists(path.dirname(config.LOG_FILE_LOCATION)):
            makedirs(path.dirname(config.LOG_FILE_LOCATION))
        self._path_to_log = config.LOG_FILE_LOCATION + 'bot.log'

    def log(self, row):
        with open(self._path_to_log, 'a') as log_file:
            cur_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_line = cur_datetime + ' -- ' + row + '\n'
            log_file.write(log_line)
