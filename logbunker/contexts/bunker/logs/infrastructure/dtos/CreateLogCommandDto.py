from typing import Any

from pydantic import BaseModel, Field


class CreateLogCommandDto(BaseModel):

    id: str = Field(example='c5285ee9-1599-46c4-bb9e-1876ef64c72b')
    content: Any = Field(example='test message')
    level: str = Field(example='info')
    origin: str = Field(example='esp8266/721653')
    type: str = Field(example='message')
    trace: str = Field(example='962c493a-b9a2-40fa-a295-005b02e7fa29')
    creation_date: str = Field(alias='creation-date', example='2022-02-16T19:08:33.327Z')
