from src.contexts.backoffice.logs.domain.LogRepository import LogRepository
from src.contexts.backoffice.logs.domain.entities.Log import Log
from src.contexts.backoffice.logs.domain.entities.LogId import LogId
from src.contexts.shared.domain.EventBus import EventBus


class LogCreator:

    def __init__(self, log_repository: LogRepository, event_bus: EventBus):
        self.__log_repository = log_repository
        self.__event_bus = event_bus

    async def run(self, log_id: LogId):
        log: Log = Log.create(log_id)
        await self.__log_repository.create_one(log)
        await self.__event_bus.publish(log.pull_domain_events())
