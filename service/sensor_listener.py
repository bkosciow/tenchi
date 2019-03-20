import socket
from message_listener.server import Server
from iot_message.message import Message
from handler.node_one_handler import NodeOneHandler
from service.handler_dispatcher import HandlerDispatcher
from service.config import Config
from service.storage import Storage


class SensorListener(object):
    def __init__(self):
        config = Config()
        self.storage = Storage()
        msg = Message(config.get('node_name'))

        broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # address = (config.get('ip', '<broadcast>'), int(config.get('port')))

        dispatcher = HandlerDispatcher(self.storage)

        svr = Server(msg)
        svr.add_handler('NodeOne', NodeOneHandler(dispatcher))
        svr.start()

    def get(self, node_name, key):
        return self.storage.get(node_name, key)
