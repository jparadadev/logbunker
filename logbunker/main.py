import argparse

from logbunker.apps.all.boot_all import boot_all
from logbunker.apps.bunker.boot import boot as boot_bunker
from logbunker.apps.backoffice.backend.boot import boot as boot_backoffice


service_mapping = {
    'bunker': boot_bunker,
    'backoffice': boot_backoffice,
    'all': boot_all,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--service',
        type=str,
        nargs='?',
        help='Service to run must be one of ["bunker", "backoffice", "all"]',
    )
    params = vars(parser.parse_args())
    service_name = params['service']
    service_booter = service_mapping[service_name]
    print(f'Booting {service_name} server')
    service_booter()
    print(f'{service_name} server start success')


if __name__ == "__main__":
    main()
