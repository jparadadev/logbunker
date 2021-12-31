import random
from datetime import timedelta, datetime


class DatetimeMother:

    @staticmethod
    def random() -> datetime:
        d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.now()
        random_date = DatetimeMother.__random_date_between(d1, d2)
        return random_date

    @staticmethod
    def __random_date_between(start: datetime, end: datetime) -> datetime:
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        return start + timedelta(seconds=random_second)
