# -*- coding: utf-8 -*-
# Created by Said at 14/11/24

from fastapi import FastAPI

from common.connection_states import CLOSE_CONNECTION
from common.models.message import Message

server = FastAPI()


@server.post('/')
async def send_message(message: Message):
    content = message.content.strip()
    if content.upper() == CLOSE_CONNECTION:
        return {'response': 'Connection closed'}
    return {'response': content.upper()}
