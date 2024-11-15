# -*- coding: utf-8 -*-
# Created by Said at 14/11/24

import asyncio

import websockets

SERVER = 'ws://127.0.0.1:5000/'


async def start_client():
    async with websockets.connect(SERVER) as websocket:
        print('Connected to server.')

        while True:
            message = input('Enter message for server: ')
            await websocket.send(message)

            response = await websocket.recv()
            print(f'Server response: {response}')

            if response == 'DESCONEXION':
                print('Server has closed the connection.')
                break


if __name__ == '__main__':
    asyncio.run(start_client())
