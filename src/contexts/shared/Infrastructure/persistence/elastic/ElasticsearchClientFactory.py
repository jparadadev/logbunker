from typing import Dict, Optional

from elasticsearch import Elasticsearch

from src.contexts.shared.Infrastructure.persistence.elastic.ElasticsearchConfiguration import ElasticsearchConfiguration


class ElasticsearchClientFactory:

    __clients: Dict[str, Elasticsearch] = {}

    @staticmethod
    def __get_client(context_name: str):
        return ElasticsearchClientFactory.__clients.get(context_name)

    @staticmethod
    def __add_client(context_name: str, client: Elasticsearch):
        ElasticsearchClientFactory.__clients[context_name] = client

    @staticmethod
    def create_instance(context_name: str, config: Optional[ElasticsearchConfiguration] = None) -> Elasticsearch:
        client = ElasticsearchClientFactory.__get_client(context_name)
        if client is not None:
            return client

        if config is None:
            config = ElasticsearchConfiguration()
        client = config.create_client_from_config()
        ElasticsearchClientFactory.__add_client(context_name, client)
        return client
