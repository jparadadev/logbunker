import os
from typing import Any

from logbunker.contexts.shared.Infrastructure.environment.EnvVar import EnvVar


class EnvManager:

    @staticmethod
    def get(var_name: EnvVar, parser: Any = None) -> Any:
        value = os.getenv(var_name.value)
        if parser is not None and value is not None:
            value = parser(value)
        return value
