"""Backward-compatibility shim — real implementation is in multi_agent/subagent.py."""
from CLAW_2024_06_19_CLAW_MULTI_AGENT_V01.subagent import (  # noqa: F401
    AgentDefinition,
    SubAgentTask,
    SubAgentManager,
    load_agent_definitions,
    get_agent_definition,
    _extract_final_text,
    _agent_run,
    _BUILTIN_AGENTS,
)
