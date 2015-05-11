from unittest import TestCase
import json
import responses

import hrpg

__author__ = 'meessg'

DEFAULT_TAG_KEYS = [
    '0f005e95-3140-4482-b94b-1eaa0e6135d6',
    '2a19221b-a88d-48e5-8f23-4ce5f29868cf',
    'ba3b805d-4eec-42d8-8bd9-77c24c983f0d']




# @responses.activate
# def getUserMocked():
#     print "111"
#     print "222"
#     return user


class TestUser(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.resp = responses.RequestsMock()

    def setUp(self):
        self.resp.add(responses.RequestsMock.GET,
                     'https://habitrpg.com/api/v2/user',
                     body=file('user_response.txt', 'rb').read(),
                     status=200,
                     content_type='application/json')

        with self.resp:
            self.user = hrpg.User('555', '***')

    def tearDown(self):
        self.resp.reset()

    def test_todos(self):
        self.assertEqual( len(self.user.todos), 3)

    def test_todo_checklist_items(self):
        items = self.user.todos['f8d08886-9306-469e-baf2-a109398a7bea'].checklist
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].text, "support for tags")
        self.assertEqual(items[1].text, "support for tasks")
        self.assertTrue(items[0].completed)
        self.assertFalse(items[1].completed)


    def test_tags(self):
        self.assertEqual(len(self.user.tags), 3)
        for key in DEFAULT_TAG_KEYS:
            self.assertIn(key, self.user.tags)
