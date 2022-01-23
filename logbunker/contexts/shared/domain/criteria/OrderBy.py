from logbunker.contexts.shared.domain.criteria.OrderAttribute import OrderAttribute
from logbunker.contexts.shared.domain.criteria.OrderDirection import OrderDirection


class OrderBy:

    def __init__(self, attr: OrderAttribute, direction: OrderDirection):
        self.attribute = attr
        self.direction = direction
