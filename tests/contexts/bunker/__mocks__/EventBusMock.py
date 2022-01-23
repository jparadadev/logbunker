from typing import List

from logbunker.contexts.shared.domain.BaseObject import BaseObject
from logbunker.contexts.shared.domain.DomainEvent import DomainEvent
from logbunker.contexts.shared.domain.EventBus import EventBus
from logbunker.contexts.shared.domain.EventSubscriber import EventSubscriber


class EventBusMock(BaseObject, EventBus):

    def start(self):
        pass

    async def publish(self, events: List[DomainEvent]):
        pass

    def add_subscribers(self, subscribers: List[EventSubscriber]):
        pass
