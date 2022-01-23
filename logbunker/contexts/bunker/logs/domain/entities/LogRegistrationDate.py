from datetime import datetime

from logbunker.contexts.shared.domain.valueobj.ValueObject import ValueObject


class LogRegistrationDate(ValueObject):

    def __init__(self, value: datetime):
        super().__init__(value)
