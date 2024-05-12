from dataclasses import dataclass
from cabletype import CableType


@dataclass
class Cable:
    type: CableType = None
    color: str = None
    length: float = None
    location: str = None