import unittest

from src.contexts.bunker.logs.application.createone.LogCreator import LogCreator
from src.contexts.bunker.logs.domain.entities.Log import Log
from tests.contexts.bunker.__mocks__.EventBusMock import EventBusMock
from tests.contexts.bunker.__mocks__.LogRepositoryMock import LogRepositoryMock
from tests.contexts.bunker.__mothers__.LogMother import LogMother
from tests.utils.async_test_decorator import async_test


class TestLogCreator(unittest.TestCase):

    def setUp(self):
        self.mocked_repo = LogRepositoryMock()
        self.mocked_event_bus = EventBusMock()
        self.log_creator: LogCreator = LogCreator(self.mocked_repo, self.mocked_event_bus)

    @async_test
    async def test_create_user(self):
        """
        Creates log.
        """
        log: Log = LogMother.random()
        await self.log_creator.run(log.id, log.content, log.level, log.origin,
                                   log.type, log.trace, log.creation_date)
        self.mocked_repo.assert_create_one_has_been_called_with(log)
