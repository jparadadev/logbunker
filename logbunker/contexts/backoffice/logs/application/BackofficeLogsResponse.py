from typing import List, Any

from logbunker.contexts.backoffice.logs.domain.entities.BackofficeLog import BackofficeLog
from logbunker.contexts.shared.domain.Metadata import Metadata
from logbunker.contexts.shared.domain.Response import Response


class BackofficeLogsResponse(Response):

    def __init__(
            self,
            logs: List[BackofficeLog],
            metadata: Metadata = None,
    ):
        self.__logs = logs
        self.__meta = metadata

    def to_primitives(self) -> Any:
        json_logs = [log.to_primitives() for log in self.__logs]
        response = {
            'data': json_logs,
        }
        if self.__meta is not None:
            response['metadata'] = self.__meta.to_dict()
        return response
