# -*- coding: utf-8 -*-
# Created by Said at 14/11/24

from pydantic import BaseModel


class Message(BaseModel):
    content: str

    @classmethod
    def receive_message(cls, data: str) -> 'Message':
        return cls(content=data.strip().upper())

    def is_close_connection(self) -> bool:
        return self.content == 'CLOSE_CONNECTION'

    def upper(self) -> str:
        return self.content.upper()
