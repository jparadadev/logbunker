from datetime import datetime
from typing import NoReturn

from logbunker.contexts.bunker.logs.application.createone.CreateLogCommand import CreateLogCommand
from logbunker.contexts.bunker.logs.application.createone.LogCreator import LogCreator
from logbunker.contexts.bunker.logs.domain.entities.LogContent import LogContent
from logbunker.contexts.bunker.logs.domain.entities.LogCreationDate import LogCreationDate
from logbunker.contexts.bunker.logs.domain.entities.LogId import LogId
from logbunker.contexts.bunker.logs.domain.entities.LogLevel import LogLevel
from logbunker.contexts.bunker.logs.domain.entities.LogOrigin import LogOrigin
from logbunker.contexts.bunker.logs.domain.entities.LogTrace import LogTrace
from logbunker.contexts.bunker.logs.domain.entities.LogType import LogType
from logbunker.contexts.shared.domain.BaseObject import BaseObject
from logbunker.contexts.shared.domain.CommandHandler import CommandHandler


class CreateLogCommandHandler(BaseObject, CommandHandler):

    __subscription: str = CreateLogCommand.COMMAND_TYPE

    def __init__(self, creator: LogCreator):
        self.__creator = creator

    def subscribed_to(self) -> str:
        return self.__subscription

    async def handle(self, command: CreateLogCommand) -> NoReturn:
        log_id = LogId(command.log_id)
        content = LogContent(command.log_content)
        level = LogLevel(command.log_level)
        origin = LogOrigin(command.log_origin)
        trace = LogTrace(command.log_trace)
        log_type = LogType(command.log_type)
        creation_date = LogCreationDate(datetime.fromisoformat(command.log_creation_date))

        await self.__creator.run(log_id, content, level, origin, log_type, trace, creation_date)


