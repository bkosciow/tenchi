from component.intent.response import Response as IntentResponse
from service.storage.storage import Storage
from intent.intent_interface import IntentInterface
from service.config import Config
from iot_message.message import Message
import socket
import json
import i18n


class RelayIntent(IntentInterface):
    action2event = {
        'enable': 'channel.on',
        'disable': 'channel.off'
    }

    def __init__(self):
        self.storage = Storage()
        self.config = Config()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.address = (
            self.config.get('node.ip'), int(self.config.get('node.port'))
        )

    def handle(self, request):
        response = IntentResponse(request)

        self._update_request_and_last(request)

        if request.data['action'] == 'enabled_state':
            response = self._state(request, response)
        else:
            response = self._toggle(request, response)

        return response

    def _update_request_and_last(self, request):
        if request.data['room'] == '':
            request.data['room'] = self.storage.get_last_value('room')

        if request.data['device'] == '':
            request.data['device'] = self.storage.get_last_value('device')

        if request.data['action'] == '':
            request.data['action'] = self.storage.get_last_value('action')

        self.storage.set_last_value('room', request.data['room'])
        self.storage.set_last_value('device', request.data['device'])
        self.storage.set_last_value('action', request.data['action'])

    def _state(self, request, response):
        sensor_response = self.storage.get_sensor_response(request.data['room'], 'relay')
        if sensor_response.code == 400:
            response.text = sensor_response.value
        else:
            response.text = i18n.t("main.relay.is_enabled") if sensor_response.value[0] \
                else i18n.t("main.relay.is_disabled")

        return response

    def _toggle(self, request, response):
        response.text = i18n.t("main.relay.enabled") if request.data['action'] == 'enable' \
            else i18n.t("main.relay.disabled")

        msg = Message(self.config.get('node.name'))

        message = msg.prepare_message({
            'targets': [request.data['room']],
            'event': self.action2event[request.data['action']],
            'parameters': {
                'channel': 0
            }
        })

        message = json.dumps(message)
        self.socket.sendto(message.encode(), self.address)

        return response
