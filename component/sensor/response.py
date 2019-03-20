
class Response(object):
    def __init__(self, value="", code=200):
        self.code = code
        self.value = "" if value is None else value

    def __str__(self):
        return "code: "+str(self.code)+", value: "+str(self.value)
