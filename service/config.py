from configparser import ConfigParser


class Config(object):
    data = {}
    file = "config.ini"

    def __init__(self):
        pass

    def get(self, key, default=None):
        section = 'general'
        if "." in key:
            section, key = key.split(".")
        return self.data.get(section, key) if self.data.get(section, key) else default

    @classmethod
    def load_config(cls):
        cls.data = ConfigParser()
        cls.data.read(cls.file)

