import socket
import json

address = ('192.168.1.255', 5053)

packet_off = {
    'protocol': 'iot:1',
    'node': 'computer',
    'chip_id': 'd45656b45afb58b1f0a46',
    'event': 'channel.off',
    'parameters': {
        'channel': 0
    },
    'targets': [
        'node-north'
    ]
}
packet_on = {
    'protocol': 'iot:1',
    'node': 'computer',
    'chip_id': 'd45656b45afb58b1f0a46',
    'event': 'channel.on',
    'parameters': {
        'channel': 0
    },
    'targets': [
        'node-north'
    ]
}
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
msg = json.dumps(packet_on)
print(msg)
s.sendto(msg.encode(), address)
