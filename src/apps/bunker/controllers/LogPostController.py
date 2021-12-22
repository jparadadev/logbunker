from typing import Dict, Any

from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.bunker.controllers.BunkerController import BunkerController
from src.contexts.bunker.logs.application.createone.CreateLogCommand import CreateLogCommand
from src.contexts.bunker.logs.infrastructure.JsonResponseErrorHandler import JsonResponseErrorHandler
from src.contexts.shared.domain.CommandBus import CommandBus
from src.contexts.shared.domain.errors.DomainError import DomainError


class LogPostController(BunkerController):

    def __init__(
            self,
            command_bus: CommandBus,
    ):
        self.__command_bus = command_bus
        self.__error_handler = JsonResponseErrorHandler()

    async def run(self, req: Request) -> JSONResponse:
        body: Dict[str, Any] = await req.json()
        command: CreateLogCommand = CreateLogCommand(body['id'], body['content'], body['level'], body['origin'],
                                                     body['creation-date'])
        try:
            await self.__command_bus.dispatch(command)
        except DomainError as err:
            return self.__error_handler.resolve(err)

        return JSONResponse(status_code=HTTPStatus.CREATED)
