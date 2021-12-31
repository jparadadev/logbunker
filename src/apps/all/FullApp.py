from fastapi import FastAPI, APIRouter

from src.apps.bunker.routes import register_routes as register_bunker_routes
from src.apps.backoffice.backend.routes import register_routes as register_backoffice_routes


class FullApp:

    def __init__(self):
        self.__app: FastAPI = FastAPI()
        bunker_router: APIRouter = APIRouter()
        register_bunker_routes(bunker_router)
        self.__app.include_router(bunker_router, prefix='/bunker/api')

        backoffice_router: APIRouter = APIRouter()
        register_backoffice_routes(backoffice_router)
        self.__app.include_router(backoffice_router, prefix='/bunker/api')

    def get_runnable(self):
        return self.__app
