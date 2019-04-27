import sys
import os
from nose.tools import assert_equal
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(ROOT_DIR, '..'))
from service import language


class TestLanguageService(object):
    def test_convert_pl_to_pl_PL(self):
        assert_equal(language.normalize('pl'), 'pl_PL')

    def test_convert_enus_to_en_US(self):
        assert_equal(language.normalize('en-us'), 'en_US')

    def test_convert_enGB_to_en_GB(self):
        assert_equal(language.normalize('en-us'), 'en_US')