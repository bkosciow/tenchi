from component.intent.response import Response as IntentResponse

class SensorIntent(object):
    # texts = {}

    def __init__(self):
        pass
        # self.sensor_listener = sensor_listener
        # self.last = {
        #     'room': '',
        #     'sensor': '',
        # }
        # self._load_texts()

    def handle(self, request):
        response = IntentResponse()
        response.lang = request.lang
        response.data = request.data
        response.intent_name = request.intent_name
        response.text = 'written text'
        response.speech = 'spoken text'

        return response

    # def _load_texts(self):
    #     self.texts = {
    #         'default': 'Nie wiem',
    #         'temp': "Temperatura wynosi {} stopni",
    #         'humi': "Wilgotość wynosi {} procent",
    #         'isLight': 'Jest jasno',
    #         'isDark': 'Jest ciemno',
    #         'isMovement': 'Ktoś sie rusza',
    #         'noMovement': 'Nie ma nikogo'
    #     }

    # def handle(self, data):
    #     if data['pokoje'] == '':
    #         data['pokoje'] = self.last['room']
    #     if data['sensor'] == '':
    #         data['sensor'] = self.last['sensor']
    #
    #     self.last['room'] = data['pokoje']
    #     self.last['sensor'] = data['sensor']
    #
    #     return self._make_response(
    #         data, self.sensor_listener.get(data['pokoje'], data['sensor'])
    #     )

    # def _make_response(self, data, sensor_response):
    #     print(sensor_response)
    #     if sensor_response.code == 400:
    #         text_response = sensor_response.value
    #     else:
    #         if data['sensor'] == 'temp':
    #             text_response = self.texts[data['sensor']].format(str(sensor_response.value))
    #         elif data['sensor'] == 'humi':
    #             text_response = self.texts[data['sensor']].format(str(sensor_response.value))
    #         elif data['sensor'] == "light":
    #             text_response = self.texts['isLight'] if sensor_response.value else self.texts['isDark']
    #         elif data['sensor'] == "pir":
    #             text_response = self.texts['isMovement'] if sensor_response.value else self.texts['noMovement']
    #
    #     return text_response
    