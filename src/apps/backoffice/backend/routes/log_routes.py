import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter

from src.apps.backoffice.backend.controllers.LogGetController import LogGetController
from src.apps.backoffice.backend.dependencies.BackofficeContainer import BackofficeContainer, backoffice_container
from src.apps.bunker.controllers.LogPostController import LogPostController
from src.apps.bunker.dependencies.BunkerContainer import BunkerContainer, bunker_container


@inject
def register(
        router: APIRouter,
        log_get_controller: LogGetController = Provide[BackofficeContainer.log_get_controller],
):
    router.add_route('/logs', log_get_controller.run, ['GET'])


backoffice_container.wire(modules=[sys.modules[__name__]])
