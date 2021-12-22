from typing import Any

from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Command import Command


class CreateLogCommand(BaseObject, Command):

    COMMAND_TYPE: str = 'bunker.log.createone'

    def __init__(
            self,
            log_id: str,
            log_content: Any,
            log_level: str,
            log_origin: str,
            log_creation_date: str,
    ):
        self.log_id = log_id
        self.log_content = log_content
        self.log_level = log_level
        self.log_origin = log_origin
        self.log_creation_date = log_creation_date

    def get_command_type_name(self) -> str:
        return self.COMMAND_TYPE
