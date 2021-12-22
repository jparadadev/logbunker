from typing import NoReturn

from src.contexts.bunker.logs.application.createone.CreateLogCommand import CreateLogCommand
from src.contexts.bunker.logs.application.createone.LogCreator import LogCreator
from src.contexts.bunker.logs.domain.entities.LogId import LogId
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.CommandHandler import CommandHandler


class CreateLogCommandHandler(BaseObject, CommandHandler):

    __subscription: str = CreateLogCommand.COMMAND_TYPE

    def __init__(self, creator: LogCreator):
        self.__creator = creator

    def subscribed_to(self) -> str:
        return self.__subscription

    async def handle(self, command: CreateLogCommand) -> NoReturn:
        log_id: LogId = LogId(command.log_id)
        await self.__creator.run(log_id)


