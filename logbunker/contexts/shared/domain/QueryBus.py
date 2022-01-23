from abc import abstractmethod

from logbunker.contexts.shared.domain.Response import Response
from logbunker.contexts.shared.domain.Interface import Interface
from logbunker.contexts.shared.domain.Query import Query


class QueryBus(Interface):

    @abstractmethod
    async def ask(self, query: Query) -> Response:
        raise NotImplementedError()
