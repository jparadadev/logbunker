from abc import ABC
from typing import Tuple, List, Optional

from logbunker.contexts.backoffice.logs.domain.entities.BackofficeLog import BackofficeLog
from logbunker.contexts.shared.domain.CriteriaQueryMetadata import CriteriaQueryMetadata
from logbunker.contexts.shared.domain.criteria.Criteria import Criteria


class BackofficeLogRepository(ABC):

    async def find_all_by_criteria(self, criteria: Criteria) -> Tuple[List[BackofficeLog],
                                                                      Optional[CriteriaQueryMetadata]]:
        raise NotImplementedError()
