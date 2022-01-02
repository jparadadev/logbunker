from typing import NoReturn

from src.contexts.bunker.logs.domain.entities.Log import Log
from src.contexts.shared.domain.Interface import Interface


class LogRepository(Interface):

    async def create_one(self, log: Log) -> NoReturn:
        raise NotImplementedError()
