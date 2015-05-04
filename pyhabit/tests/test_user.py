from unittest import TestCase
import json
import responses

import hrpg

__author__ = 'meessg'

responses.add(responses.GET,
              'https://habitrpg.com/api/v2/user',
              body=file('user_response.txt', 'rb').read(),
              status=200,
              content_type='application/json')

DEFAULT_TAG_KEYS = [
    '0f005e95-3140-4482-b94b-1eaa0e6135d6',
    '2a19221b-a88d-48e5-8f23-4ce5f29868cf',
    'ba3b805d-4eec-42d8-8bd9-77c24c983f0d' ]

class TestUser(TestCase):


    @responses.activate
    def test_tags(self):

        user = hrpg.User('555', '***')

        self.assertEqual( len(user.tags), 3)
        for key in DEFAULT_TAG_KEYS:
            self.assertIn(key, user.tags)