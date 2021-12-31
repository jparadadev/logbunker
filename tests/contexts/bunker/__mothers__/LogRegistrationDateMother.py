from datetime import datetime

from src.contexts.bunker.logs.domain.entities.LogRegistrationDate import LogRegistrationDate
from tests.utils.mothers.DatetimeMother import DatetimeMother


class LogRegistrationDateMother:

    @staticmethod
    def create(registration_date: datetime) -> LogRegistrationDate:
        return LogRegistrationDate(registration_date)

    @staticmethod
    def random() -> LogRegistrationDate:
        return LogRegistrationDateMother.create(DatetimeMother.random())

    @staticmethod
    def with_params(registration_date: datetime = None) -> LogRegistrationDate:
        if registration_date is None:
            return LogRegistrationDateMother.random()
        return LogRegistrationDateMother.create(registration_date)
