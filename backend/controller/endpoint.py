from dataclasses import dataclass
from enum import Enum
from typing import List


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"


@dataclass
class Endpoint:
    path: str
    methods: List[HttpMethod]

