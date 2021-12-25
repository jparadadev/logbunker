import uvicorn

from src.apps.all.FullApp import FullApp
from src.apps.bunker.BunkerApp import BunkerApp
from src.contexts.shared.Infrastructure.environment.EnvManager import EnvManager
from src.contexts.shared.Infrastructure.environment.EnvVar import EnvVar


class FullServer:

    def __init__(self):
        self.app = FullApp()

    def run(self):
        host = EnvManager.get(EnvVar.BUNKER_SERVER_HOST)
        port = EnvManager.get(EnvVar.BUNKER_SERVER_PORT, parser=int)
        uvicorn.run(self.app.get_runnable(), host=host, port=port)
