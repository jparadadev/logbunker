from src.contexts.bunker.logs.domain.entities.LogType import LogType
from tests.utils.mothers.WordMother import WordMother


class LogTypeMother:

    @staticmethod
    def create(log_type: str) -> LogType:
        return LogType(log_type)

    @staticmethod
    def random() -> LogType:
        return LogTypeMother.create(WordMother.random())

    @staticmethod
    def with_params(log_type: str = None) -> LogType:
        if log_type is None:
            return LogTypeMother.random()
        return LogTypeMother.create(log_type)
