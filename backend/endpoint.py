from dataclasses import dataclass
from typing import List


GET = "GET"
POST = "POST"


@dataclass
class Endpoint:
    path: str
    methods: List[str]

GENERATE_IMAGE = Endpoint(
    path="/generate",
    methods=[POST]
)
PING = Endpoint(
    path="/ping",
    methods=[GET]
)