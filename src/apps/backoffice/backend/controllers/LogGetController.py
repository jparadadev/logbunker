from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.backoffice.backend.controllers.BackofficeController import BackofficeController
from src.contexts.backoffice.logs.application.findall.FindLogsByCriteriaQuery import FindLogsByCriteriaQuery
from src.contexts.bunker.logs.infrastructure.JsonResponseErrorHandler import JsonResponseErrorHandler
from src.contexts.shared.Infrastructure.parsers.parse_dict_format_to_criteria import parse_dict_to_criteria
from src.contexts.shared.domain.Query import Query
from src.contexts.shared.domain.QueryBus import QueryBus
from src.contexts.shared.domain.Response import Response
from src.contexts.shared.domain.errors.DomainError import DomainError


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


