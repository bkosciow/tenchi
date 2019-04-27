from component.intent.response import Response as IntentResponse
from service.storage.storage import Storage
import i18n


class SensorIntent(object):
    def __init__(self):
        self.storage = Storage()
        self.last = {
            'room': '',
            'sensor': '',
        }

    def handle(self, request):
        response = IntentResponse()
        response.lang = request.lang
        response.data = request.data
        response.intent_name = request.intent_name

        self._update_request_and_last(request)

        sensor_response = self.storage.get(request.data['room'], request.data['sensor'])
        response.text = self._get_text(request.data, sensor_response)

        return response

    def _update_request_and_last(self, request):
        if request.data['room'] == '':
            request.data['room'] = self.last['room']

        if request.data['sensor'] == '':
            request.data['sensor'] = self.last['sensor']

        self.last['room'] = request.data['room']
        self.last['sensor'] = request.data['sensor']

    def _get_text(self, data, sensor_response):
        text_response = ""
        if sensor_response.code == 400:
            text_response = sensor_response.value
        else:
            if data['sensor'] == 'temp':
                text_response = i18n.t("main.sensor.temperature", value=sensor_response.value)
            elif data['sensor'] == 'humi':
                text_response = i18n.t("main.sensor.humidity", value=sensor_response.value)
            elif data['sensor'] == "light":
                text_response = i18n.t("main.sensor.light.on") if sensor_response.value else i18n.t("main.sensor.light.off")
            elif data['sensor'] == "pir":
                text_response = i18n.t("main.sensor.movement.detected") if sensor_response.value else i18n.t(
                    "main.sensor.movement.undetected")

        return text_response
