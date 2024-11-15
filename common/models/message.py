# -*- coding: utf-8 -*-
# Created by Said at 14/11/24

from pydantic import BaseModel


class Message(BaseModel):
    content: str
