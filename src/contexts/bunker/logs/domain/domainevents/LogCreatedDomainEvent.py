from datetime import datetime
from typing import Any, Optional

from src.contexts.shared.domain.DomainEvent import DomainEvent


class LogCreatedDomainEvent(DomainEvent):

    EVENT_TYPE = 'bunker.log.created'

    def __init__(
            self,
            aggregate_id: str,
            log_content: Any,
            log_level: str,
            log_origin: str,
            log_creation_date: datetime,
            log_registration_date: datetime,
            event_id: Optional[str] = None,
            occurred_on: Optional[datetime] = None,
    ):
        super().__init__(self.EVENT_TYPE, aggregate_id, event_id, occurred_on)
        self.log_content = log_content
        self.log_level = log_level
        self.log_origin = log_origin
        self.log_creation_date = log_creation_date
        self.log_registration_date = log_registration_date

    def to_primitives(self) -> Any:
        return {
            'data': {
                'id': self.id,
                'aggregate-id': self.aggregate_id,
                'occurred-on': self.occurred_on,
                'created-at': self.created_at,
                'type': LogCreatedDomainEvent.EVENT_TYPE,
                'attributes': {
                    'content': self.log_content,
                    'level': self.log_level,
                    'origin': self.log_origin,
                    'creation-date': self.log_creation_date,
                    'registration-date': self.log_registration_date,
                },
            },
            'meta': {
                'attempts': 0,
            }
        }
