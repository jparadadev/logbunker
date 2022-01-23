from logbunker.contexts.shared.domain.criteria.FilterField import FilterField
from logbunker.contexts.shared.domain.criteria.FilterOperator import FilterOperator
from logbunker.contexts.shared.domain.criteria.FilterValue import FilterValue


class Filter:

    def __init__(self, field: FilterField, operator: FilterOperator, value: FilterValue):
        self.field = field
        self.operator = operator
        self.value = value
