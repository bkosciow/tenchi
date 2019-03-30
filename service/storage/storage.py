from component.sensor.response import Response
import abc


class StorageEngineInterface(metaclass=abc.ABCMeta):
    def set(self, key, value):
        pass

    def get(self, key):
        pass

    def exists(self, key):
        pass


class Storage(object):
    engine = None

    def set(self, node_name, params):
        if not self.engine.exists(node_name):
            self.engine.set(node_name, {})

        data = self.engine.get(node_name)
        for p in params:
            data[p] = params[p]

        self.engine.set(node_name, data)

    def get(self, node_name, key):
        if not self.engine.exists(node_name):
            return Response("I do not know this room", 400)

        data = self.engine.get(node_name)
        if key in data:
            return Response(data[key])
        else:
            return Response("I have no such data", 400)

    def get_all(self):
        return self.engine.data

    @classmethod
    def set_engine(cls, engine):
        cls.engine = engine
