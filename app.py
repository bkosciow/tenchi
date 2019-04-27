# -*- coding: utf-8 -*-
import os
import sys

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(ROOT_DIR, '..'))

from flask import Flask
from flask import request
from flask import jsonify
from flask_basicauth import BasicAuth
from pprint import pprint
from service.intent_dispatcher import IntentDispatcher
from intent.sensor import SensorIntent
from component.intent.request import Request as IntentRequest
from component.intent.response import Response as IntentResponse
from service.sensor_listener import SensorListener
from service.config import Config
from service.storage.dictionary_engine import DictionaryEngine
from service.storage.storage import Storage
from service import language
import i18n
i18n.load_path.append('./translation')

Storage.set_engine(DictionaryEngine())

Config.load_config()
config = Config()

intents = IntentDispatcher()
intents.add('sensors', SensorIntent())

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = config.get('assistant.login')
app.config['BASIC_AUTH_PASSWORD'] = config.get('assistant.password')
basic_auth = BasicAuth(app)

sensorListener = SensorListener()


@app.route("/tenchi", methods=['GET', 'POST'])
@basic_auth.required
def tenchi():
    content = request.get_json()
    pprint(content['queryResult']['intent']['displayName'])
    pprint(content['queryResult']['parameters'])

    intent_request = IntentRequest()
    intent_request.intent_name = content['queryResult']['intent']['displayName']
    intent_request.lang = language.normalize(content['queryResult']['languageCode'])
    intent_request.data = content['queryResult']['parameters']
    i18n.set('locale', intent_request.lang)

    if intents.supports(intent_request):
        intent_response = intents.handle(intent_request)
    else:
        intent_response = IntentResponse()
        intent_response.text = i18n.t('main.intent.not_supported', intent=intent_request.intent_name)

    response = {}
    response["payload"] = {
        "google": {
            "richResponse": {
                "items": [
                    {
                        "simpleResponse": {
                            "textToSpeech": intent_response.speech,
                            "displayText": intent_response.text,
                        }
                    }
                ]
            }
        }
    }

    print(response)
    return jsonify(response)


@app.route("/storage")
def storage():
    storage = Storage()
    return jsonify(storage.get_all())


@app.route("/ping")
def ping():
    return "pong"


if __name__ == "__main__":
    app.run(
        host=config.get('ip'),
        port=config.get('port'),
        debug=True
    )
