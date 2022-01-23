from typing import NoReturn

from logbunker.contexts.bunker.logs.domain.entities.Log import Log
from logbunker.contexts.shared.domain.Interface import Interface


class LogRepository(Interface):

    async def create_one(self, log: Log) -> NoReturn:
        raise NotImplementedError()
