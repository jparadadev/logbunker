from abc import ABC, abstractmethod
from typing import Any, Dict, NoReturn

from elasticsearch import Elasticsearch


class ElasticsearchRepository(ABC):

    def __init__(self, client: Elasticsearch):
        self.__client = client

    @abstractmethod
    def get_index_name(self) -> str:
        raise NotImplementedError()

    async def _create_one(self, doc_id: str, raw_obj: Dict[str, Any]) -> NoReturn:
        self.__client.create(id=doc_id, document=raw_obj, index=self.get_index_name())
