from typing import List

from logbunker.contexts.shared.domain.criteria.Filter import Filter
from logbunker.contexts.shared.domain.criteria.Limit import Limit
from logbunker.contexts.shared.domain.criteria.OrderBy import OrderBy


class Criteria:

    def __init__(
            self,
            filters: List[Filter] = None,
            order: OrderBy = None,
            limit: Limit = None,
    ):
        self.filters = filters
        self.order = order
        self.limit = limit
