# -*- coding: utf-8 -*-
# Created by Said at 14/11/24

from fastapi import FastAPI

from common.models.message import Message

server = FastAPI()


@server.post('/message')
async def send_message(message: Message):
    content = message.content.strip()
    if content.upper() == "DESCONEXION":
        return {"response": "Connection closed"}
    return {"response": content.upper()}
