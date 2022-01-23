from logbunker.contexts.shared.domain.criteria import UpperLimit
from logbunker.contexts.shared.domain.criteria.LimitOffset import LimitOffset


class Limit:

    def __init__(self, lower: LimitOffset, upper: UpperLimit):
        self.lower = lower
        self.upper = upper
