import socket
import json
from iot_message.message import Message

address = ('192.168.1.255', 5053)
#
# packet_off = {
#     'protocol': 'iot:1',
#     'node': 'computer',
#     'chip_id': 'd45656b45afb58b1f0a46',
#     'event': 'channel.off',
#     'parameters': {
#         'channel': 0
#     },
#     'targets': [
#         'node-north'
#     ]
# }
# packet_on = {
#     'protocol': 'iot:1',
#     'node': 'computer',
#     'chip_id': 'd45656b45afb58b1f0a46',
#     'event': 'channel.on',
#     'parameters': {
#         'channel': 0
#     },
#     'targets': [
#         'node-north'
#     ]
# }
#
# packet_status = {
#     'protocol': 'iot:1',
#     'node': 'computer',
#     'chip_id': 'd45656b45afb58b1f0a46',
#     'event': 'channel.states',
#     'parameters': {},
#     'targets': [
#         'node-living'
#     ]
# }

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
print(msg)
s.sendto(msg.encode(), address)
