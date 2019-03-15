"""Handler for DHT11"""
from message_listener.abstract.handler_interface import \
    Handler as HandlerInterface


class DHTHandler(HandlerInterface):
    def handle(self, message):
        """handle a message"""
        if message is not None \
                and 'event' in message and message['event'] == 'dht.status':
                self.worker.set_sensor_data(
                    message['node'],
                    {
                        'temp': str(message['parameters']['temp']),
                        'humi': str(message['parameters']['humi'])
                    }
                )
