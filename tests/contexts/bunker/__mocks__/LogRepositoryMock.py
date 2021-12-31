from typing import NoReturn, List
from unittest.mock import Mock

from src.contexts.bunker.logs.domain.LogRepository import LogRepository
from src.contexts.bunker.logs.domain.entities.Log import Log
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.criteria.Criteria import Criteria
from tests.contexts.bunker.__matchers__.LogMatcher import LogMatcher


class LogRepositoryMock(BaseObject, LogRepository):

    def __init__(self):
        self.__create_one_mock = Mock()

    async def find_by_criteria(self, criteria: Criteria) -> List[Log]:
        raise NotImplementedError()

    # ----------------------------------------------------
    # ------------------ CREATE ONE ----------------------
    # ----------------------------------------------------

    async def create_one(self, log: Log) -> NoReturn:
        self.__create_one_mock(log)

    def assert_create_one_has_been_called(self):
        assert self.__create_one_mock.called

    def assert_create_one_has_been_called_with(self, log: Log):
        log_matcher = LogMatcher(log)
        self.__create_one_mock.assert_called_with(log_matcher)
