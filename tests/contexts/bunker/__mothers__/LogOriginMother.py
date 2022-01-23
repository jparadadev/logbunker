from logbunker.contexts.bunker.logs.domain.entities.LogLevel import LogLevel
from logbunker.contexts.bunker.logs.domain.entities.LogOrigin import LogOrigin
from tests.utils.mothers.WordMother import WordMother


class LogOriginMother:

    @staticmethod
    def create(origin: str) -> LogOrigin:
        return LogOrigin(origin)

    @staticmethod
    def random() -> LogOrigin:
        return LogOriginMother.create(WordMother.random())

    @staticmethod
    def with_params(origin: str = None) -> LogOrigin:
        if origin is None:
            return LogOriginMother.random()
        return LogOriginMother.create(origin)
