from src.contexts.backoffice.logs.application.BackofficeLogsResponse import BackofficeLogsResponse
from src.contexts.backoffice.logs.domain.BackofficeLogRepository import BackofficeLogRepository
from src.contexts.shared.domain.criteria.Criteria import Criteria


class LogsByCriteriaFinder:

    def __init__(self, log_repository: BackofficeLogRepository):
        self.__log_repository = log_repository

    async def run(self, criteria: Criteria) -> BackofficeLogsResponse:
        logs, criteria_metadata = await self.__log_repository.find_all_by_criteria(criteria)
        return BackofficeLogsResponse(logs, criteria_metadata)

