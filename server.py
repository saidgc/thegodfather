# -*- coding: utf-8 -*-
# Created by Said at 14/11/24

import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from common.models.message import Message
from common.logger_utils import logger

server = FastAPI()


@server.websocket('/')
async def send_message(web_socket: WebSocket):
    await web_socket.accept()
    logger.info('Connected to client.')
    try:
        while True:
            data = await web_socket.receive_text()
            logger.info(f'Received message: {data}')
            message = Message.receive_message(data)

            if message.is_close_connection():
                logger.info('Closing connection with client.')
                await web_socket.send_text('Connection closed')
                logger.info('Connection closed.')
                break

            logger.info(f'Sending message: {message.upper()}')
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
