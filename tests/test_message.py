# -*- coding: utf-8 -*-
# Created by Said at 14/11/24

import unittest
from common.models.message import Message


class TestMessageModel(unittest.TestCase):

    def test_receive_message(self):
        message = Message.receive_message('hello')

        self.assertEqual(message.content, 'HELLO')

    def test_is_close_connection(self):
        message = Message(content='CLOSE_CONNECTION')

        self.assertTrue(message.is_close_connection())

    def test_upper(self):
        message = Message(content='hello')

        self.assertEqual(message.upper(), 'HELLO')


if __name__ == '__main__':
    unittest.main()
