from component.intent.response import Response as IntentResponse
from service.storage import Storage


class SensorIntent(object):
    # texts = {}

    def __init__(self):
        self.storage = Storage()
        self.last = {
            'room': '',
            'sensor': '',
        }
        self._load_texts()

    def handle(self, request):
        response = IntentResponse()
        response.lang = request.lang
        response.data = request.data
        response.intent_name = request.intent_name

        if request.data['room'] == '':
            request.data['room'] = self.last['room']

        if request.data['sensor'] == '':
            request.data['sensor'] = self.last['sensor']

        self.last['room'] = request.data['room']
        self.last['sensor'] = request.data['sensor']

        sensor_response = self.storage.get(request.data['room'], request.data['sensor'])
        response.text = self._get_text(request.data, sensor_response)

        return response

    def _load_texts(self):
        self.texts = {
            'default': "I don't know",
            'temp': "Temperature is {}",
            'humi': "Humidity is {} percent",
            'isLight': 'There is light',
            'isDark': 'There is dark',
            'isMovement': 'There is movement',
            'noMovement': 'No movement detected'
        }

    def _get_text(self, data, sensor_response):
        text_response = ""
        if sensor_response.code == 400:
            text_response = sensor_response.value
        else:
            if data['sensor'] == 'temp':
                text_response = self.texts[data['sensor']].format(str(sensor_response.value))
            elif data['sensor'] == 'humi':
                text_response = self.texts[data['sensor']].format(str(sensor_response.value))
            elif data['sensor'] == "light":
                text_response = self.texts['isLight'] if sensor_response.value else self.texts['isDark']
            elif data['sensor'] == "pir":
                text_response = self.texts['isMovement'] if sensor_response.value else self.texts['noMovement']

        return text_response
