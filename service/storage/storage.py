from component.sensor.response import Response
import abc
import i18n


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
            return Response(i18n.t("main.room.not_known"), 400)

        data = self.engine.get(node_name)
        if key in data:
            return Response(data[key])
        else:
            return Response(i18n.t("main.room.no_data"), 400)

    def get_all(self):
        return self.engine.data

    @classmethod
    def set_engine(cls, engine):
        cls.engine = engine
