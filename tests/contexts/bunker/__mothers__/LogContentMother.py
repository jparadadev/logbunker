from logbunker.contexts.bunker.logs.domain.entities.LogContent import LogContent
from tests.utils.mothers.WordMother import WordMother


class LogContentMother:

    @staticmethod
    def create(log_content: str) -> LogContent:
        return LogContent(log_content)

    @staticmethod
    def random() -> LogContent:
        return LogContentMother.create(WordMother.random())

    @staticmethod
    def with_params(log_content: str = None) -> LogContent:
        if log_content is None:
            return LogContentMother.random()
        return LogContentMother.create(log_content)
