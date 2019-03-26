"""Used to get data from handlers and pass it to correct widget"""


class HandlerDispatcher(object):
    """class HandlerDispatcher"""
    def __init__(self, storage):
        self.storage = storage

    def set_sensor_data(self, node, data):
        self.storage.set(node, data)

    # def set_relay_states(self, node, states):
    #     """get data from relay"""
    #     if node in self.widgets:
    #         list(map(lambda item: item.change_values({
    #             'states': states
    #         }), self.widgets[node]))
