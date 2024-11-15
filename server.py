# -*- coding: utf-8 -*-
# Created by Said at 14/11/24

import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from common.models.message import Message

server = FastAPI()


@server.websocket('/')
async def send_message(web_socket: WebSocket):
    await web_socket.accept()
    try:
        while True:
            data = await web_socket.receive_text()
            message = Message.receive_message(data)

            if message.is_close_connection():
                await web_socket.send_text('Connection closed')
                break

            await web_socket.send_text(message.upper())

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
