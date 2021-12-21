from datetime import datetime
from typing import Any, Optional

from src.contexts.shared.domain.DomainEvent import DomainEvent
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class LogCreatedDomainEvent(DomainEvent):

    EVENT_TYPE = 'bunker.log.created'

    def __init__(
            self,
            aggregate_id: str,
            event_id: Optional[str] = None,
            occurred_on: Optional[datetime] = None,
    ):
        super().__init__(self.EVENT_TYPE, aggregate_id, event_id, occurred_on)

    def to_primitives(self) -> Any:
        return {
            'data': {
                'id': self.id,
                'aggregate-id': self.aggregate_id,
                'occurred-on': self.occurred_on,
                'created-at': self.created_at,
                'type': LogCreatedDomainEvent.EVENT_TYPE,
                'attributes': None,
            },
            'meta': {
                'attempts': 0,
            }
        }
