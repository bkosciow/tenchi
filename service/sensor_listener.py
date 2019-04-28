import socket
from message_listener.server import Server
from iot_message.message import Message
from handler.node_one_handler import NodeOneHandler
from service.config import Config
from service.storage.storage import Storage


class SensorListener(object):
    def __init__(self):
        config = Config()
        self.storage = Storage()
        msg = Message(config.get('node.name'))

        broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # address = (config.get('ip', '<broadcast>'), int(config.get('port')))

        svr = Server(msg)
        svr.add_handler('NodeOne', NodeOneHandler(self.storage))
        svr.start()

    def get(self, node_name, key):
        return self.storage.get(node_name, key)
