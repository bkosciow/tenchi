from .storage import StorageEngineInterface


class DictionaryEngine(StorageEngineInterface):
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data[key]

    def exists(self, key):
        return key in self.data
