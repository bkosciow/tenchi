from message_listener.abstract.handler_interface import \
    Handler as HandlerInterface


class NodeOneHandler(HandlerInterface):
    def handle(self, message):
        if message is not None and 'event' in message:
            if message['event'] == 'dht.status':
                self.worker.set_sensor_param(
                    message['node'],
                    {
                        'temp': str(message['parameters']['temp']),
                        'humi': str(message['parameters']['humi'])
                    }
                )
            if message['event'] == 'detect.light':
                self.worker.set_sensor_param(
                    message['node'],
                    {'light': True}
                )

            if message['event'] == 'detect.dark':
                self.worker.set_sensor_param(
                    message['node'],
                    {'light': False}
                )
            if message['event'] == 'pir.movement':
                self.worker.set_sensor_param(
                    message['node'],
                    {'pir': True}
                )

            if message['event'] == 'pir.nomovement':
                self.worker.set_sensor_param(
                    message['node'],
                    {'pir': False}
                )

            if message['event'] == 'channels.response':
                self.worker.set_sensor_param(
                    message['node'],
                    {'relay': message['response']}
                )
