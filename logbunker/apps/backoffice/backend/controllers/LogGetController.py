from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from logbunker.apps.backoffice.backend.controllers.BackofficeController import BackofficeController
from logbunker.contexts.backoffice.logs.application.findall.FindLogsByCriteriaQuery import FindLogsByCriteriaQuery
from logbunker.contexts.bunker.logs.infrastructure.JsonResponseErrorHandler import JsonResponseErrorHandler
from logbunker.contexts.shared.Infrastructure.parsers.parse_dict_format_to_criteria import parse_dict_to_criteria
from logbunker.contexts.shared.domain.Query import Query
from logbunker.contexts.shared.domain.QueryBus import QueryBus
from logbunker.contexts.shared.domain.Response import Response
from logbunker.contexts.shared.domain.errors.DomainError import DomainError


class LogGetController(BackofficeController):

    def __init__(
            self,
            query_bus: QueryBus,
    ):
        self.__query_bus = query_bus
        self.__error_handler = JsonResponseErrorHandler()

    async def run(self, req: Request) -> JSONResponse:
        query_params = dict(req.query_params)
        filters, order_by, limit = parse_dict_to_criteria(query_params)
        query: Query = FindLogsByCriteriaQuery(filters, order_by, limit)
        try:
            res: Response = await self.__query_bus.ask(query)
            return JSONResponse(status_code=HTTPStatus.OK, content=res.to_primitives())
        except DomainError as err:
            return self.__error_handler.resolve(err)


