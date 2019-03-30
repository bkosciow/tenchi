# -*- coding: utf-8 -*-
import os
import sys

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(ROOT_DIR, '..'))

from flask import Flask
from flask import request
from flask import jsonify
from pprint import pprint
from service.intent_dispatcher import IntentDispatcher
from intent.sensor import SensorIntent
from component.intent.request import Request as IntentRequest
from component.intent.response import Response as IntentResponse
from service.sensor_listener import SensorListener
from service.config import Config
from service.storage.dictionary_engine import DictionaryEngine
from service.storage.storage import Storage

Storage.set_engine(DictionaryEngine())

Config.load_config()

intents = IntentDispatcher()
intents.add('sensors', SensorIntent())

app = Flask(__name__)
sensorListener = SensorListener()


@app.route("/tenchi", methods=['GET', 'POST'])
def tenchi():
    content = request.get_json()
    pprint(content['queryResult']['intent']['displayName'])
    pprint(content['queryResult']['languageCode'])
    pprint(content['queryResult']['parameters'])

    intent_request = IntentRequest()
    intent_request.intent_name = content['queryResult']['intent']['displayName']
    intent_request.lang = content['queryResult']['languageCode']
    intent_request.data = content['queryResult']['parameters']

    if intents.supports(intent_request):
        intent_response = intents.handle(intent_request)
    else:
        intent_response = IntentResponse()
        intent_response.text = "Intent {} not supported".format(intent_request.intent_name)

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

# @app.route("/mokona", methods=['GET', 'POST'])
# def hello():
#     content = request.get_json()
#     intentName = content['queryResult']['intent']['displayName']
#     pprint(content['queryResult']['intent']['displayName'])
#     pprint(content['queryResult']['parameters'])
#     data = content['queryResult']['parameters']
#
#     if intents.supports(intentName):
#         txt = intents.handle(intentName, data)
#         # txt = "test"
#     else:
#         txt = "Intent {} not supported".format(intentName)
#         print(txt)
#
#     response = {}
#     response["fulfillmentText"] = txt
#     response["payload"] = {
#         "google": {
#             "richResponse": {
#                 "items": [
#                     {
#                         "simpleResponse": {
#                             "textToSpeech": txt
#                         }
#                     }
#                 ]
#             }
#         }
#     }
#     return jsonify(response)


@app.route("/ping")
def ping():
    return "pong"


if __name__ == "__main__":
    app.run(
        host='0.0.0.0', #config.get('ip', 'general'),
        port=7777, #config.get('port', 'general'),
        debug=True
    )
