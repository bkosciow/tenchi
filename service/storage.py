from component.sensor.response import Response


class Storage(object):
    data = {}

    def set(self, node_name, params):
        if node_name not in self.data:
            self.data[node_name] = {}

        for p in params:
            self.data[node_name][p] = params[p]

    def get(self, node_name, key):
        if node_name in self.data:
            if key in self.data[node_name]:
                return Response(self.data[node_name][key])
            else:
                return Response("I have no such data", 400)

        return Response("I do not know this room", 400)

    def get_all(self):
        return self.data

