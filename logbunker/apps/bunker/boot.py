from logbunker.apps.bunker.BunkerServer import BunkerServer


def boot():
    server = BunkerServer()
    server.run()
