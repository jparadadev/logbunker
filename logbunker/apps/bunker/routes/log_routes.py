import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from starlette.requests import Request

from logbunker.apps.bunker.controllers.LogPostController import LogPostController
from logbunker.apps.bunker.dependencies.BunkerContainer import BunkerContainer, bunker_container
from logbunker.contexts.bunker.logs.infrastructure.dtos.CreateLogCommandDto import CreateLogCommandDto


@inject
def register(
        router: APIRouter,
        log_post_controller: LogPostController = Provide[BunkerContainer.log_post_controller],
):
    @router.post('/logs', tags=["Logs"])
    async def run_wrapper(_: CreateLogCommandDto, req: Request):
        return await log_post_controller.run(req)


bunker_container.wire(modules=[sys.modules[__name__]])
