from logbunker.contexts.shared.domain.valueobj.ValueObject import ValueObject


class LogOrigin(ValueObject):

    def __init__(self, value: str):
        super().__init__(value)
