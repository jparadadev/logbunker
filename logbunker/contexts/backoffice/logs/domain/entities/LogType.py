from logbunker.contexts.shared.domain.valueobj.ValueObject import ValueObject


class LogType(ValueObject):

    def __init__(self, value: str):
        super().__init__(value)
