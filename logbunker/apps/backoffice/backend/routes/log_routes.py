import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from starlette.requests import Request

from logbunker.apps.backoffice.backend.controllers.LogGetController import LogGetController
from logbunker.apps.backoffice.backend.dependencies.BackofficeContainer import BackofficeContainer, backoffice_container


@inject
def register(
        router: APIRouter,
        log_get_controller: LogGetController = Provide[BackofficeContainer.log_get_controller],
):
    @router.get('/logs', tags=['Logs'])
    async def run_wrapper(req: Request):
        return await log_get_controller.run(req)


backoffice_container.wire(modules=[sys.modules[__name__]])
