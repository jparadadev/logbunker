from datetime import datetime

from logbunker.contexts.bunker.logs.domain.entities.LogContent import LogContent
from logbunker.contexts.bunker.logs.domain.entities.LogCreationDate import LogCreationDate
from logbunker.contexts.bunker.logs.domain.entities.LogId import LogId
from logbunker.contexts.bunker.logs.domain.entities.LogLevel import LogLevel
from logbunker.contexts.bunker.logs.domain.entities.LogOrigin import LogOrigin
from logbunker.contexts.bunker.logs.domain.entities.LogRegistrationDate import LogRegistrationDate
from logbunker.contexts.bunker.logs.domain.entities.LogTrace import LogTrace
from logbunker.contexts.bunker.logs.domain.entities.LogType import LogType
from logbunker.contexts.bunker.logs.domain.entities.Log import Log
from tests.contexts.bunker.__mothers__.LogContentMother import LogContentMother
from tests.contexts.bunker.__mothers__.LogCreationDateMother import LogCreationDateMother
from tests.contexts.bunker.__mothers__.LogIdMother import LogIdMother
from tests.contexts.bunker.__mothers__.LogLevelMother import LogLevelMother
from tests.contexts.bunker.__mothers__.LogOriginMother import LogOriginMother
from tests.contexts.bunker.__mothers__.LogRegistrationDateMother import LogRegistrationDateMother
from tests.contexts.bunker.__mothers__.LogTraceMother import LogTraceMother
from tests.contexts.bunker.__mothers__.LogTypeMother import LogTypeMother


class LogMother:

    @staticmethod
    def create(
            log_id: LogId,
            content: LogContent,
            level: LogLevel,
            origin: LogOrigin,
            log_type: LogType,
            trace: LogTrace,
            creation_date: LogCreationDate,
            registration_date: LogRegistrationDate = None,
    ) -> Log:
        return Log(log_id, content, level, origin, log_type, trace, creation_date, registration_date)

    @staticmethod
    def random() -> Log:
        return LogMother.create(
            LogIdMother.random(),
            LogContentMother.random(),
            LogLevelMother.random(),
            LogOriginMother.random(),
            LogTypeMother.random(),
            LogTraceMother.random(),
            LogCreationDateMother.random(),
            LogRegistrationDateMother.random(),
        )

    @staticmethod
    def with_params(
            log_id: str = None,
            log_content: str = None,
            log_level: str = None,
            origin: str = None,
            log_type: str = None,
            trace: str = None,
            creation_date: datetime = None,
            registration_date: datetime = None,
    ) -> Log:
        return LogMother.create(
            LogIdMother.with_params(log_id),
            LogContentMother.with_params(log_content),
            LogLevelMother.with_params(log_level),
            LogOriginMother.with_params(origin),
            LogTypeMother.with_params(log_type),
            LogTraceMother.with_params(trace),
            LogCreationDateMother.with_params(creation_date),
            LogRegistrationDateMother.with_params(registration_date),
        )
