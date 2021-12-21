from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Command import Command


class CreateLogCommand(BaseObject, Command):

    COMMAND_TYPE: str = 'bunker.log.createone'

    def __init__(self, log_id: str):
        self.log_id = log_id

    def get_command_type_name(self) -> str:
        return self.COMMAND_TYPE
