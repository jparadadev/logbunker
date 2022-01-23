from abc import abstractmethod
from typing import Any

from logbunker.contexts.shared.domain.Command import Command
from logbunker.contexts.shared.domain.Interface import Interface


class CommandBus(Interface):

    @abstractmethod
    async def dispatch(self, command: Command) -> Any:
        raise NotImplementedError()
