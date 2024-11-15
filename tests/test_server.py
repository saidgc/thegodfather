# -*- coding: utf-8 -*-
# Created by Said at 14/11/24
import unittest
import asyncio
import websockets
import subprocess
import time

SERVER_URL = 'ws://127.0.0.1:5000/'


class TestWebSocketServer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server_process = subprocess.Popen(['python', 'server.py'])
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()
        cls.server_process.wait()

    async def connect_and_send_message(self, message):
        async with websockets.connect(SERVER_URL) as websocket:
            await websocket.send(message)
            response = await websocket.recv()
            return response

    def test_server_response(self):
        message = 'Hello, Server!'
        expected_response = 'HELLO, SERVER!'

        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(self.connect_and_send_message(message))

        self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
