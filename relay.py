import socket
import json
from iot_message.message import Message

address = ('192.168.1.255', 5053)
message_builder = Message('node_name')
msg = message_builder.prepare_message({
    'event': 'channel.off',
    'parameters': {
        'channel': 0
    },

})

msg['targets'] = ['node-north']

print(msg)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
msg = json.dumps(msg)
s.sendto(msg.encode(), address)
