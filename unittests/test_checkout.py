from features.steps.checkout import parse_raw_cookie
from unittest import TestCase


class TestCheckout(TestCase):

    def test_parse_raw_cookie(self):
        raw_cookie = "BITRIX_SM_location_type=%D0%B3; BX_USER_ID=d7f73fbc427128ca6efecedd7e6a08d2; __tld__=null"

        parsed = parse_raw_cookie(raw_cookie)
        self.assertEqual(type(parsed), dict)

        expected = {"BITRIX_SM_location_type": "%D0%B3", "BX_USER_ID": "d7f73fbc427128ca6efecedd7e6a08d2", "__tld__": "null"}
        for key in parsed:
            self.assertTrue(key in expected)
            self.assertEqual(expected[key], parsed[key])