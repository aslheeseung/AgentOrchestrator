from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Task:
    description: str
    tags: List[str] = field(default_factory=list)


@dataclass
class AgentResponse:
    agent_name: str
    summary: str
    details: Dict[str, str] = field(default_factory=dict)


@dataclass
class Agent:
    name: str
    role: str
    capabilities: List[str]

    def can_handle(self, task: Task) -> bool:
        return any(tag in self.capabilities for tag in task.tags)

    def handle(self, task: Task) -> AgentResponse:
        return AgentResponse(
            agent_name=self.name,
            summary=f"{self.name} handled task: {task.description}",
            details={"role": self.role},
        )


class DatabaseAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            name="Database Agent",
            role="Query literature, datasets, and lab records.",
            capabilities=["database", "literature", "dataset"],
        )


class ComputationAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            name="Computation Agent",
            role="Run simulations, ML inference, and analytics.",
            capabilities=["compute", "simulation", "analysis"],
        )


class ExperimentalAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            name="Experimental Agent",
            role="Plan experiments, protocols, and instrument usage.",
            capabilities=["experiment", "protocol", "instrument"],
        )


class SkillIntegrationAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            name="Skill Integration Agent",
            role="Register user skills and custom agents.",
            capabilities=["skill", "custom", "integration"],
        )
