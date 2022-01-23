from enum import Enum


class EnvVar(Enum):

    ENV_MODE = 'env_mode'

    # -------------------------------------------------------
    # ---------------------- BUNKER -------------------------
    # -------------------------------------------------------

    BUNKER_SERVER_HOST = 'bunker.server.host'
    BUNKER_SERVER_PORT = 'bunker.server.port'

    # -------------------------------------------------------
    # ------------------------ LOG --------------------------
    # -------------------------------------------------------

    SHARED_LOG_MONGO_HOST   = 'shared.log.mongo.host'
    SHARED_LOG_MONGO_PORT   = 'shared.log.mongo.port'

    SHARED_LOG_ELASTIC_HOST = 'shared.log.elastic.host'
    SHARED_LOG_ELASTIC_PORT = 'shared.log.elastic.port'
