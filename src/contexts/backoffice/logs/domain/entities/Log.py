from typing import Optional, Dict, List, Union, Any

from src.contexts.backoffice.logs.domain.domainevents.LogCreatedDomainEvent import LogCreatedDomainEvent
from src.contexts.backoffice.logs.domain.entities.LogId import LogId
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class Log(AggregateRoot):

    def __init__(self, log_id: LogId):
        super().__init__()
        self.id = log_id

    @staticmethod
    def create(user_id: LogId):
        log = Log(user_id)
        event = LogCreatedDomainEvent(log.id.value())
        log.record_event(event)
        return log

    @staticmethod
    def create_from_primitives(raw_data: Dict[str, Any]):
        user = Log(
            LogId(raw_data.get('id')),
        )
        return user

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'id': self.id.value(),
        }
