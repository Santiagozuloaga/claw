"""Multi-agent package for clawspring.

Provides:
  - AgentDefinition  — typed agent definition (name, system_prompt, model, tools)
  - SubAgentTask     — lifecycle-tracked task
  - SubAgentManager  — thread-pool manager for spawning agents
  - load_agent_definitions / get_agent_definition — agent registry
"""
import importlib; _m_subagent = importlib.import_module(".2024-06-19_CLAW_SUBAGENT_V01", __package__); globals().update({'AgentDefinition': getattr(_m_subagent, 'AgentDefinition'), 'SubAgentTask': getattr(_m_subagent, 'SubAgentTask'), 'SubAgentManager': getattr(_m_subagent, 'SubAgentManager'), 'load_agent_definitions': getattr(_m_subagent, 'load_agent_definitions'), 'get_agent_definition': getattr(_m_subagent, 'get_agent_definition')})

__all__ = [
    "AgentDefinition",
    "SubAgentTask",
    "SubAgentManager",
    "load_agent_definitions",
    "get_agent_definition",
]
