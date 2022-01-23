from typing import Any

from logbunker.contexts.shared.domain.valueobj.ValueObject import ValueObject


class LogContent(ValueObject):

    def __init__(self, value: Any):
        super().__init__(value)
