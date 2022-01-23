import uvicorn

from logbunker.apps.bunker.BunkerApp import BunkerApp
from logbunker.contexts.shared.Infrastructure.environment.EnvManager import EnvManager
from logbunker.contexts.shared.Infrastructure.environment.EnvVar import EnvVar


class BunkerServer:

    def __init__(self):
        self.app = BunkerApp()

    def run(self):
        host = EnvManager.get(EnvVar.BUNKER_SERVER_HOST)
        port = EnvManager.get(EnvVar.BUNKER_SERVER_PORT, parser=int)
        uvicorn.run(self.app.get_runnable(), host=host, port=port)
