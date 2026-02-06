from dataclasses import dataclass
from typing import Dict


@dataclass
class Skill:
    name: str
    description: str
    metadata: Dict[str, str]
