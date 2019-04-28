import abc


class IntentInterface(metaclass=abc.ABCMeta):
    def handle(self, request):
        pass
