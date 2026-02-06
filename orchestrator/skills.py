from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Skill:
    name: str
    description: str
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, str] = field(default_factory=dict)
