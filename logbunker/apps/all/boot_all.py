from logbunker.apps.all.FullServer import FullServer


def boot_all():
    server = FullServer()
    server.run()
