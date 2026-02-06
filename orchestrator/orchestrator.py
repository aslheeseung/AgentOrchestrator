from dataclasses import dataclass, field
from typing import Dict, Iterable, List

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

    def _skill_tags(self, task: Task) -> Iterable[str]:
        tags: List[str] = []
        for skill_name in task.required_skills:
            skill = self.skills.get(skill_name)
            if skill:
                tags.extend(skill.tags)
        return tags

    def _augment_task(self, task: Task) -> Task:
        augmented_tags = list(dict.fromkeys(task.tags + list(self._skill_tags(task))))
        for agent in self.agents:
            augmented_tags.extend(agent.suggest_tags(task))
        task.tags = list(dict.fromkeys(augmented_tags))
        return task

    def route(self, task: Task) -> List[Agent]:
        task = self._augment_task(task)
        matched = [agent for agent in self.agents if agent.can_handle(task)]
        if matched:
            return sorted(matched, key=lambda agent: agent.priority, reverse=True)
        return sorted(self.agents, key=lambda agent: agent.priority, reverse=True)

    def run(self, task: Task) -> List[AgentResponse]:
        responses = []
        for agent in self.route(task):
            responses.append(agent.handle(task))
        return responses
