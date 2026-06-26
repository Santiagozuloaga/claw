"""Multi-agent package for clawspring.

Provides:
  - AgentDefinition  — typed agent definition (name, system_prompt, model, tools)
  - SubAgentTask     — lifecycle-tracked task
  - SubAgentManager  — thread-pool manager for spawning agents
  - load_agent_definitions / get_agent_definition — agent registry
"""
from CLAW_2026_06_24_MULTI_AGENT_V01.subagent import (
    AgentDefinition,
    SubAgentTask,
    SubAgentManager,
    load_agent_definitions,
    get_agent_definition,
)

__all__ = [
    "AgentDefinition",
    "SubAgentTask",
    "SubAgentManager",
    "load_agent_definitions",
    "get_agent_definition",
]
