import sys
import os
from nose.tools import assert_equal
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(ROOT_DIR, '..'))
from service.config import Config

CFG_FILE = ROOT_DIR + "/assets/config_test.ini"
Config.file = CFG_FILE
Config.load_config()


class TestConfigService(object):
    def setUp(self):
        self.cfg = Config()

    def test_config_name_should_change(self):
        assert_equal(self.cfg.file, CFG_FILE)

    def test_get_value_from_default_section(self):
        assert_equal(self.cfg.get('port'), '5053')

    def test_get_value_from_section_general(self):
        assert_equal(self.cfg.get('general.port'), '5053')

    def test_get_login_from_section_assistant(self):
        assert_equal(self.cfg.get('assistant.login'), 'rambo')