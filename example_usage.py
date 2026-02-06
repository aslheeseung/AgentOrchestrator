from orchestrator import (
    ComputationAgent,
    DatabaseAgent,
    ExperimentalAgent,
    Orchestrator,
    Skill,
    SkillIntegrationAgent,
    Task,
)


def main() -> None:
    orchestrator = Orchestrator()
    orchestrator.register_agent(DatabaseAgent())
    orchestrator.register_agent(ComputationAgent())
    orchestrator.register_agent(ExperimentalAgent())
    orchestrator.register_agent(SkillIntegrationAgent())

    orchestrator.register_skill(
        Skill(
            name="XRD-Peak-Analysis",
            description="Analyze XRD spectra and extract peaks.",
            metadata={"owner": "user"},
        )
    )

    task = Task(
        description="Find recent datasets for lithium-sulfur batteries and run a baseline analysis.",
        tags=["dataset", "analysis"],
    )

    for response in orchestrator.run(task):
        print(f"{response.agent_name}: {response.summary}")


if __name__ == "__main__":
    main()
