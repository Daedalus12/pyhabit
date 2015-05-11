from datetime import datetime
from api import convert_HRPG_datestring_to_datetime, \
    convert_datetime_to_HRPG_datestring
from unittest import TestCase


class TestDatetimeConversions(TestCase):
    def test_convert_HRPG_datestring_to_datetime(self):
        result = convert_HRPG_datestring_to_datetime(
            "2015-05-04T19:36:35.278Z")
        expected = datetime(2015, 5, 4, 19, 36, 35)
        self.assertLess((result-expected).total_seconds(), 1)

    def test_convert_datetime_to_HRPG_datestring(self):
        t = datetime(2015, 5, 4, 19, 36, 35)
        result = convert_datetime_to_HRPG_datestring(t)
        expected = "2015-05-04T19:36:35.000Z"
        self.assertEqual(result, expected)