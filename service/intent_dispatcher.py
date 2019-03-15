

class IntentDispatcher(object):
    _intents = {}

    def add(self, name, _class):
        self._intents[name] = _class

    def handle(self, request):
        return self._intents[request.intent_name].handle(request)

    def supports(self, request):
        return request.intent_name in self._intents
