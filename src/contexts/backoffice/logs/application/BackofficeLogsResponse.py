from typing import List, Any

from src.contexts.backoffice.logs.domain.entities.Log import Log
from src.contexts.shared.domain.CriteriaQueryMetadata import CriteriaQueryMetadata
from src.contexts.shared.domain.Metadata import Metadata
from src.contexts.shared.domain.Response import Response


class BackofficeUsersResponse(Response):

    def __init__(
            self,
            logs: List[Log],
            metadata: Metadata = None,
    ):
        self.__users = logs
        self.__meta = metadata

    def to_primitives(self) -> Any:
        json_logs = [log.to_primitives() for log in self.__users]
        response = {
            'data': json_logs,
        }
        if self.__meta is not None:
            response['metadata'] = self.__meta.to_dict()
        return response
