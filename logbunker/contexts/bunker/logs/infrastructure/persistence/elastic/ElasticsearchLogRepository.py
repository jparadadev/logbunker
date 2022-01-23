import datetime
from typing import NoReturn

from elasticsearch import Elasticsearch

from logbunker.contexts.bunker.logs.domain.LogRepository import LogRepository
from logbunker.contexts.bunker.logs.domain.entities.Log import Log
from logbunker.contexts.bunker.logs.domain.errors.LogAlreadyExistsError import LogAlreadyExistsError
from logbunker.contexts.shared.Infrastructure.persistence.elastic.ElasticsearchRepository import ElasticsearchRepository


class ElasticsearchLogRepository(ElasticsearchRepository, LogRepository):

    __INDEX_NAME = 'log-bunker'

    def __init__(self, client: Elasticsearch):
        super().__init__(client)

    def get_index_name(self) -> str:
        return f'{self.__INDEX_NAME}-{datetime.date.today().isoformat()}'

    async def create_one(self, log: Log) -> NoReturn:
        try:
            await super()._create_one(log.id.value(), log.to_primitives())
        except Exception as e:
            raise LogAlreadyExistsError('Log with ID <{}> already exists.'.format(log.id.value()))
