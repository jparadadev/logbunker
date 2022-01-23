from typing import List

from logbunker.contexts.shared.domain.Query import Query
from logbunker.contexts.shared.domain.criteria.Filter import Filter
from logbunker.contexts.shared.domain.criteria.Limit import Limit
from logbunker.contexts.shared.domain.criteria.OrderBy import OrderBy


class FindLogsByCriteriaQuery(Query):

    QUERY_TYPE: str = 'find-bunker-logs-by-criteria'

    def __init__(
            self,
            filters: List[Filter],
            order_by: OrderBy = None,
            limit: Limit = None,
    ):
        self.filters = filters
        self.order_by = order_by
        self.limit = limit

    def get_query_type_name(self) -> str:
        return self.QUERY_TYPE
