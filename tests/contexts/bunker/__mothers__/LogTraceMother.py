from src.contexts.bunker.logs.domain.entities.LogTrace import LogTrace
from tests.utils.mothers.WordMother import WordMother


class LogTraceMother:

    @staticmethod
    def create(trace: str) -> LogTrace:
        return LogTrace(trace)

    @staticmethod
    def random() -> LogTrace:
        return LogTraceMother.create(WordMother.random())

    @staticmethod
    def with_params(trace: str = None) -> LogTrace:
        if trace is None:
            return LogTraceMother.random()
        return LogTraceMother.create(trace)
