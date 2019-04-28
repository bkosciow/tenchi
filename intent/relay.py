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
