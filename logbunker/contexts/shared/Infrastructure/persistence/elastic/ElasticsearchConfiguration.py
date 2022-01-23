from elasticsearch import Elasticsearch
from pymongo import MongoClient


class ElasticsearchConfiguration:

    def __init__(
            self,
            host: str = 'localhost',
            port: int = 27017,
    ):
        self.host = host
        self.port = port

    def create_client_from_config(self) -> Elasticsearch:
        return Elasticsearch(
            host=self.host,
            port=self.port,
        )
