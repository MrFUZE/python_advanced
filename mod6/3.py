import logging
import json


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        try:
            json.dumps(msg)
            return msg, kwargs
        except TypeError:
            json_msg = json.dumps(str(msg))
            return {"message": json_msg}, kwargs


logging.basicConfig(level=logging.DEBUG, filename='skillbox_json_messages.log',
                    format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}',
                    datefmt='%H:%M:%S')



logger = JsonAdapter(logging.getLogger(__name__))
logger.info('Message with "double" quotes')
