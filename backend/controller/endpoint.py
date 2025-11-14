from dataclasses import dataclass
from enum import Enum
from typing import List


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"


@dataclass
class Endpoint:
    path: str
    _methods: List[HttpMethod]

    def methods(self) -> List[str]:
        return [method.value for method in self._methods]

GENERATE_IMAGE = Endpoint(
    path="/generate",
    _methods=[HttpMethod.POST]
)
PING = Endpoint(
    path="/ping",
    _methods=[HttpMethod.GET]
)