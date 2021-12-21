import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter

from src.apps.bunker.controllers.LogPostController import LogPostController
from src.apps.bunker.dependencies.BunkerContainer import BunkerContainer, bunker_container


@inject
def register(
        router: APIRouter,
        log_post_controller: LogPostController = Provide[BunkerContainer.log_post_controller],
):
    router.add_route('/logs', log_post_controller.run, ['POST'])


bunker_container.wire(modules=[sys.modules[__name__]])
