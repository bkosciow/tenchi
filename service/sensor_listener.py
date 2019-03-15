import time
import socket
from message_listener.server import Server
from iot_message.message import Message
from handler.DHTHandler import DHTHandler
from handler.PIRHandler import PIRHandler
from handler.LightHandler import LightHandler
# from handler.RelayHandler import RelayHandler
from service.handler_dispatcher import HandlerDispatcher
# from service.worker_handler import Handler as WorkerHandler

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

        dispatcher = HandlerDispatcher(self.storage, {
            'node-kitchen': [],
            'node-living': [],
            'node-north': [],
            'node-pc': [],
        })
        svr = Server(msg)
        svr.add_handler('dht11', DHTHandler(dispatcher))
        svr.add_handler('pir', PIRHandler(dispatcher))
        svr.add_handler('light', LightHandler(dispatcher))
        # svr.add_handler('relay', RelayHandler(dispatcher))
        svr.start()

    def get(self, node_name, key):
        return self.storage.get(node_name, key)
