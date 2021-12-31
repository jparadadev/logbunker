from src.contexts.bunker.logs.domain.entities.Log import Log


class LogMatcher:

    def __init__(self, log: Log):
        self.log = log

    def __eq__(self, log2: Log) -> bool:
        log1 = self.log
        res = log1.id.value() == log2.id.value() and \
              log1.trace == log2.trace
        return res
