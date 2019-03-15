

class Config(object):
    data = {}

    def __init__(self):
        pass

    def get(self, key, default=None):
        if key in self.data:
            return self.data[key]

        return default

    @classmethod
    def load_config(cls):
        cls.data = {
            'node_name': 'pc_assist',
            'ip': '192.168.1.255',
            'port': 5053
        }
