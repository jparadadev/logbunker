from src.contexts.bunker.logs.domain.entities.LogId import LogId
from tests.utils.mothers.WordMother import WordMother


class LogIdMother:

    @staticmethod
    def create(log_id: str) -> LogId:
        return LogId(log_id)

    @staticmethod
    def random() -> LogId:
        return LogIdMother.create(WordMother.random())

    @staticmethod
    def with_params(log_id: str = None) -> LogId:
        if log_id is None:
            return LogIdMother.random()
        return LogIdMother.create(log_id)
