from dataclasses import dataclass, field
from typing import Dict, List

from orchestrator.agents import Agent, AgentResponse, Task
from orchestrator.skills import Skill


@dataclass
class Orchestrator:
    agents: List[Agent] = field(default_factory=list)
    skills: Dict[str, Skill] = field(default_factory=dict)

    def register_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def register_skill(self, skill: Skill) -> None:
        self.skills[skill.name] = skill

    def route(self, task: Task) -> List[Agent]:
        matched = [agent for agent in self.agents if agent.can_handle(task)]
        return matched or self.agents

    def run(self, task: Task) -> List[AgentResponse]:
        responses = []
        for agent in self.route(task):
            responses.append(agent.handle(task))
        return responses
