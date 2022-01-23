import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter

from logbunker.apps.bunker.controllers.StatusGetController import StatusGetController
from logbunker.apps.bunker.dependencies.BunkerContainer import BunkerContainer, bunker_container


@inject
def register(
        router: APIRouter,
        status_get_controller: StatusGetController = Provide[BunkerContainer.status_get_controller]
):
    router.add_route('/status', status_get_controller.run)


bunker_container.wire(modules=[sys.modules[__name__]])
