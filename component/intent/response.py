

class Response(object):
    def __init__(self, request=None):
        self.intent_name = request.intent_name if request else ''
        self.lang = request.lang if request else ''
        self.data = request.data if request else ''
        self._speech = ''
        self._text = ''

    @property
    def text(self):
        if self._text == '':
            return self._speech
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def speech(self):
        if self._speech == '':
            return self._text
        return self._speech

    @speech.setter
    def speech(self, value):
        self._speech = value
