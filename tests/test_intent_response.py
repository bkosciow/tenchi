import sys
import os
from nose.tools import assert_equal
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(ROOT_DIR, '..'))
from component.intent.request import Request
from component.intent.response import Response


class TestIntentResponse(object):
    def test_create_response_from_request(self):
        request = Request()
        request.intent_name = 'abc'
        request.lang = 'jp_JP'
        request.data = {
            'a': 'a', 'b': 'b'
        }
        response = Response(request)

        assert_equal(response.intent_name, request.intent_name)
        assert_equal(response.lang, request.lang)
        assert_equal(response.data, request.data)

