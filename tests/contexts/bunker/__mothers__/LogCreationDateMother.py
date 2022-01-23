from datetime import datetime

from logbunker.contexts.bunker.logs.domain.entities.LogCreationDate import LogCreationDate
from tests.utils.mothers.DatetimeMother import DatetimeMother


class LogCreationDateMother:

    @staticmethod
    def create(creation_date: datetime) -> LogCreationDate:
        return LogCreationDate(creation_date)

    @staticmethod
    def random() -> LogCreationDate:
        return LogCreationDateMother.create(DatetimeMother.random())

    @staticmethod
    def with_params(creation_date: datetime = None) -> LogCreationDate:
        if creation_date is None:
            return LogCreationDateMother.random()
        return LogCreationDateMother.create(creation_date)
