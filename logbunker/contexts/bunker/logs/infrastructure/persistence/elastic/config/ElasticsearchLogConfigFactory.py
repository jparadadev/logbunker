from logbunker.contexts.shared.Infrastructure.environment.EnvManager import EnvManager
from logbunker.contexts.shared.Infrastructure.environment.EnvVar import EnvVar
from logbunker.contexts.shared.Infrastructure.persistence.elastic.ElasticsearchConfiguration import ElasticsearchConfiguration


class ElasticsearchLogConfigFactory:

    @staticmethod
    def create() -> ElasticsearchConfiguration:
        config = ElasticsearchConfiguration(
            EnvManager.get(EnvVar.SHARED_LOG_ELASTIC_HOST),
            EnvManager.get(EnvVar.SHARED_LOG_ELASTIC_PORT, parser=int),
        )
        return config
