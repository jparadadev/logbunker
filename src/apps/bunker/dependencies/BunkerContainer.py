from dependency_injector import containers, providers

from src.apps.bunker.controllers.StatusGetController import StatusGetController
from src.apps.bunker.controllers.LogPostController import LogPostController
from src.contexts.bunker.logs.application.createone.CreateLogCommandHandler import CreateLogCommandHandler
from src.contexts.bunker.logs.application.createone.LogCreator import LogCreator
from src.contexts.bunker.logs.infrastructure.persistence.elastic.ElasticsearchLogRepository import \
    ElasticsearchLogRepository
from src.contexts.bunker.logs.infrastructure.persistence.elastic.config.ElasticsearchLogConfigFactory import \
    ElasticsearchLogConfigFactory
from src.contexts.bunker.logs.infrastructure.persistence.mongo.PyMongoLogRepository import \
    PyMongoLogRepository
from src.contexts.shared.Infrastructure.commandbus.InMemoryCommandBus import InMemoryCommandBus
from src.contexts.shared.Infrastructure.eventbus.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.Infrastructure.persistence.elastic.ElasticsearchClientFactory import ElasticsearchClientFactory


class BunkerContainer(containers.DeclarativeContainer):

    event_bus = providers.Singleton(
        InMemoryEventBus,
    )

    db_config = providers.Singleton(ElasticsearchLogConfigFactory.create)
    db_client = providers.Singleton(ElasticsearchClientFactory.create_instance, 'bunker', db_config)

    log_repository = providers.Singleton(ElasticsearchLogRepository, db_client)

    log_creator = providers.Singleton(LogCreator, log_repository, event_bus)
    create_log_command_handler = providers.Singleton(
        CreateLogCommandHandler,
        log_creator,
    )

    command_bus = providers.Singleton(
        InMemoryCommandBus,
        create_log_command_handler,
    )

    status_get_controller = providers.Singleton(StatusGetController)
    log_post_controller = providers.Singleton(LogPostController, command_bus)


bunker_container: BunkerContainer = BunkerContainer()


