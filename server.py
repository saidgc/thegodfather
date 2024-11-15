# -*- coding: utf-8 -*-
# Created by Said at 14/11/24

import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from common.connection_states import CLOSE_CONNECTION

server = FastAPI()


@server.websocket('/')
async def send_message(web_socket: WebSocket):
    await web_socket.accept()
    try:
        while True:
            message = await web_socket.receive_text()
            message = message.upper().strip()

            if message == CLOSE_CONNECTION:
                await web_socket.send_text('Connection closed')
                break

            await web_socket.send_text(message)

    except WebSocketDisconnect:
        await web_socket.close()


if __name__ == '__main__':
    config = uvicorn.Config(
        app='server:server',
        host='127.0.0.1',
        port=5000,
        log_level='info',
    )
    server = uvicorn.Server(config)
    server.run()
