from src.contexts.bunker.logs.domain.LogRepository import LogRepository
from src.contexts.bunker.logs.domain.entities.Log import Log
from src.contexts.bunker.logs.domain.entities.LogContent import LogContent
from src.contexts.bunker.logs.domain.entities.LogCreationDate import LogCreationDate
from src.contexts.bunker.logs.domain.entities.LogId import LogId
from src.contexts.bunker.logs.domain.entities.LogLevel import LogLevel
from src.contexts.bunker.logs.domain.entities.LogOrigin import LogOrigin
from src.contexts.bunker.logs.domain.entities.LogTrace import LogTrace
from src.contexts.bunker.logs.domain.entities.LogType import LogType
from src.contexts.shared.domain.EventBus import EventBus


class LogCreator:

    def __init__(self, log_repository: LogRepository, event_bus: EventBus):
        self.__log_repository = log_repository
        self.__event_bus = event_bus

    async def run(
            self,
            log_id: LogId,
            content: LogContent,
            level: LogLevel,
            origin: LogOrigin,
            log_type: LogType,
            trace: LogTrace,
            creation_date: LogCreationDate,
    ):
        log: Log = Log.create(log_id, content, level, origin, log_type, trace, creation_date)
        await self.__log_repository.create_one(log)
        await self.__event_bus.publish(log.pull_domain_events())
