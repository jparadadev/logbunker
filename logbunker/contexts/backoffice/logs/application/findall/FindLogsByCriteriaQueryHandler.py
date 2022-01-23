from logbunker.contexts.backoffice.logs.application.BackofficeLogsResponse import BackofficeLogsResponse
from logbunker.contexts.backoffice.logs.application.findall.FindLogsByCriteriaQuery import FindLogsByCriteriaQuery
from logbunker.contexts.backoffice.logs.application.findall.LogsByCriteriaFinder import LogsByCriteriaFinder
from logbunker.contexts.shared.domain.QueryHandler import QueryHandler
from logbunker.contexts.shared.domain.criteria.Criteria import Criteria


class FindLogsByCriteriaQueryHandler(QueryHandler):

    __subscription: str = FindLogsByCriteriaQuery.QUERY_TYPE

    def __init__(self, finder: LogsByCriteriaFinder):
        self.__finder = finder

    def subscribed_to(self) -> str:
        return self.__subscription

    async def handle(self, query: FindLogsByCriteriaQuery) -> BackofficeLogsResponse:
        criteria = Criteria(query.filters, query.order_by, query.limit)
        return await self.__finder.run(criteria)
