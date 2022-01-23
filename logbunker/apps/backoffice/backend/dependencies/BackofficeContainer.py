from dependency_injector import containers, providers

from logbunker.apps.backoffice.backend.controllers.LogGetController import LogGetController
from logbunker.apps.bunker.controllers.StatusGetController import StatusGetController
from logbunker.contexts.backoffice.logs.application.findall.FindLogsByCriteriaQueryHandler import \
    FindLogsByCriteriaQueryHandler
from logbunker.contexts.backoffice.logs.application.findall.LogsByCriteriaFinder import LogsByCriteriaFinder
from logbunker.contexts.backoffice.logs.infrastructure.persistence.PyMongoBackofficeLogRepository import \
    PyMongoBackofficeLogRepository
from logbunker.contexts.bunker.logs.infrastructure.persistence.mongo.config.PyMongoLogConfigFactory import PyMongoLogConfigFactory
from logbunker.contexts.shared.Infrastructure.persistence.mongo.PyMongoClientFactory import PyMongoClientFactory
from logbunker.contexts.shared.Infrastructure.querybus.InMemoryQueryBus import InMemoryQueryBus


class BackofficeContainer(containers.DeclarativeContainer):

    db_config = providers.Singleton(PyMongoLogConfigFactory.create)
    db_client = providers.Singleton(PyMongoClientFactory.create_instance, 'bunker', db_config)

    log_repository = providers.Singleton(PyMongoBackofficeLogRepository, db_client)

    log_by_criteria_finder = providers.Singleton(LogsByCriteriaFinder, log_repository)
    find_logs_by_criteria_command_handler = providers.Singleton(
        FindLogsByCriteriaQueryHandler,
        log_by_criteria_finder,
    )

    query_bus = providers.Singleton(
        InMemoryQueryBus,
        find_logs_by_criteria_command_handler,
    )

    status_get_controller = providers.Singleton(StatusGetController)
    log_get_controller = providers.Singleton(LogGetController, query_bus)


backoffice_container: BackofficeContainer = BackofficeContainer()


