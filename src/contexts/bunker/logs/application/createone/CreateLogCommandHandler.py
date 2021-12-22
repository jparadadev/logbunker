from datetime import datetime
from typing import NoReturn

from src.contexts.bunker.logs.application.createone.CreateLogCommand import CreateLogCommand
from src.contexts.bunker.logs.application.createone.LogCreator import LogCreator
from src.contexts.bunker.logs.domain.entities.LogContent import LogContent
from src.contexts.bunker.logs.domain.entities.LogCreationDate import LogCreationDate
from src.contexts.bunker.logs.domain.entities.LogId import LogId
from src.contexts.bunker.logs.domain.entities.LogLevel import LogLevel
from src.contexts.bunker.logs.domain.entities.LogOrigin import LogOrigin
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.CommandHandler import CommandHandler


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
        creation_date = LogCreationDate(datetime.fromisoformat(command.log_creation_date))

        await self.__creator.run(log_id, content, level, origin, creation_date)


