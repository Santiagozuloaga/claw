"""Backward-compatibility shim — real implementation is in multi_agent/subagent.py."""
import importlib; _mod = importlib.import_module('2024-06-19_CLAW_MULTI_AGENT_V01.subagent'); globals().update({k: getattr(_mod, k) for k in []}) # noqa: F401
    AgentDefinition,
    SubAgentTask,
    SubAgentManager,
    load_agent_definitions,
    get_agent_definition,
    _extract_final_text,
    _agent_run,
    _BUILTIN_AGENTS,
)
