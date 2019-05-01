from component.intent.response import Response as IntentResponse
from service.storage.storage import Storage
from intent.intent_interface import IntentInterface
import i18n


class SensorIntent(IntentInterface):
    def __init__(self):
        self.storage = Storage()

    def handle(self, request):
        response = IntentResponse(request)

        self._update_request_and_last(request)

        sensor_response = self.storage.get_sensor_response(request.data['room'], request.data['sensor'])
        response.text = self._get_text(request.data, sensor_response)

        return response

    def _update_request_and_last(self, request):
        if request.data['room'] == '':
            request.data['room'] = self.storage.get_last_value('room')

        if request.data['sensor'] == '':
            request.data['sensor'] = self.storage.get_last_value('sensor')

        self.storage.set_last_value('room', request.data['room'])
        self.storage.set_last_value('sensor', request.data['sensor'])

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
