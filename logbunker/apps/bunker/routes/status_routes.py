import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from starlette.requests import Request

from logbunker.apps.bunker.controllers.StatusGetController import StatusGetController
from logbunker.apps.bunker.dependencies.BunkerContainer import BunkerContainer, bunker_container


@inject
def register(
        router: APIRouter,
        status_get_controller: StatusGetController = Provide[BunkerContainer.status_get_controller]
):
    @router.get('/status', tags=["Health"])
    async def run_wrapper(req: Request):
        return await status_get_controller.run(req)


bunker_container.wire(modules=[sys.modules[__name__]])
