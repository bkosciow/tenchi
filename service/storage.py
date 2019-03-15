
class Storage(object):
    data = {}

    def change_values(self, node_name, params):
        if not node_name in self.data:
            self.data[node_name] = {}

        for p in params:
            self.data[node_name][p] = params[p]

    def get(self, node_name, key):
        if node_name in self.data:
            if key in self.data[node_name]:
                return SensorResponse(self.data[node_name][key])
            else:
                return SensorResponse("Nie mam takich danych", 400)

        return SensorResponse("Nie znam pomieszczenia", 400)


class SensorResponse(object):
    def __init__(self, value="", code=200):
        self.code = code
        self.value = "" if value is None else value

    def __str__(self):
        return "kod: "+str(self.code)+", value: "+str(self.value)
