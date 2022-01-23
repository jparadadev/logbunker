from typing import Tuple, List, Optional

from pymongo import MongoClient

from logbunker.contexts.backoffice.logs.domain.BackofficeLogRepository import BackofficeLogRepository
from logbunker.contexts.backoffice.logs.domain.entities.BackofficeLog import BackofficeLog
from logbunker.contexts.shared.Infrastructure.persistence.mongo.PyMongoRepository import PyMongoRepository
from logbunker.contexts.shared.domain.CriteriaQueryMetadata import CriteriaQueryMetadata
from logbunker.contexts.shared.domain.criteria.Criteria import Criteria


class PyMongoBackofficeLogRepository(PyMongoRepository, BackofficeLogRepository):

    __COLLECTION_NAME = 'logs'
    __DATABASE_NAME = 'logbunker'

    def __init__(self, client: MongoClient):
        super().__init__(client)

    def get_database_name(self):
        return self.__DATABASE_NAME

    def get_collection_name(self):
        return self.__COLLECTION_NAME

    async def find_all_by_criteria(self, criteria: Criteria) -> Tuple[List[BackofficeLog],
                                                                      Optional[CriteriaQueryMetadata]]:
        results, count = await super()._find_by_criteria(criteria)
        entities = [BackofficeLog.create_from_primitives(result) for result in results]
        metadata = CriteriaQueryMetadata(count)
        return entities, metadata
