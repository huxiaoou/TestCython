from dataclasses import dataclass
from typing import Literal


@dataclass
class CQuant:
    name: str
    gender: Literal["F", "M"]
    age: int
    salary: float