from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from logbunker.apps.bunker.controllers.BunkerController import BunkerController


class StatusGetController(BunkerController):

    def __init__(self):
        pass

    async def run(self, req: Request) -> JSONResponse:
        return JSONResponse(status_code=HTTPStatus.OK)
