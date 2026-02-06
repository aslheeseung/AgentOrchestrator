from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional


@dataclass
class Task:
    description: str
    tags: List[str] = field(default_factory=list)
    requested_agents: List[str] = field(default_factory=list)
    required_skills: List[str] = field(default_factory=list)


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
    priority: int = 0

    def can_handle(self, task: Task) -> bool:
        if self.name in task.requested_agents:
            return True
        return any(tag in self.capabilities for tag in task.tags)

    def suggest_tags(self, task: Task) -> Iterable[str]:
        return []

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
            priority=20,
        )


class ComputationAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            name="Computation Agent",
            role="Run simulations, ML inference, and analytics.",
            capabilities=["compute", "simulation", "analysis"],
            priority=30,
        )


class ExperimentalAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            name="Experimental Agent",
            role="Plan experiments, protocols, and instrument usage.",
            capabilities=["experiment", "protocol", "instrument"],
            priority=10,
        )


class SkillIntegrationAgent(Agent):
    def __init__(self, skill_tags: Optional[List[str]] = None) -> None:
        super().__init__(
            name="Skill Integration Agent",
            role="Register user skills and custom agents.",
            capabilities=["skill", "custom", "integration"],
            priority=100,
        )
        self.skill_tags = skill_tags or []

    def suggest_tags(self, task: Task) -> Iterable[str]:
        if task.required_skills:
            return ["skill"]
        return self.skill_tags
