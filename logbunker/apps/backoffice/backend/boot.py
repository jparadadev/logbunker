from logbunker.apps.backoffice.backend.BackofficeServer import BackofficeServer


def boot():
    server = BackofficeServer()
    server.run()
