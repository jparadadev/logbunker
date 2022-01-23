from logbunker.contexts.bunker.logs.domain.entities.LogLevel import LogLevel
from tests.utils.mothers.WordMother import WordMother


class LogLevelMother:

    @staticmethod
    def create(level: str) -> LogLevel:
        return LogLevel(level)

    @staticmethod
    def random() -> LogLevel:
        return LogLevelMother.create(WordMother.random())

    @staticmethod
    def with_params(log_level: str = None) -> LogLevel:
        if log_level is None:
            return LogLevelMother.random()
        return LogLevelMother.create(log_level)
