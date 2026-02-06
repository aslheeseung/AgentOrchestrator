# Material Science Agent Orchestrator

A lightweight, extensible agent orchestrator tailored for Material Science workflows. It provides a
multi-agent architecture with:

- **Database Agent**: query literature, datasets, lab notebooks, or internal repositories.
- **Computation Agent**: run simulations, DFT workflows, ML inference, or data analysis.
- **Experimental Agent**: handle lab protocols, instrument scheduling, and experiment tracking.
- **Skill Integration Agent**: incorporate user-provided agents or existing skills into the system.

## Architecture Overview

```
User Request
   ↓
Orchestrator → Intent routing → Agent(s)
   ↓
Skill Integration → user skills / custom agents
   ↓
Response aggregation
```

## Example Configuration

See [`example_config.yaml`](./example_config.yaml) for a minimal configuration that registers
standard agents and user-provided skills.

## Example Usage

```bash
python example_usage.py
```

This runs a simple orchestration flow and prints the selected agents and responses.
