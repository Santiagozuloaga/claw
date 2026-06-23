"""Backward-compatibility shim — real implementation is in skill/ package."""
import importlib
m_2024_06_19_CLAW_SKILL_V01_2024_06_19_CLAW_LOADER_V01 = importlib.import_module("2024-06-19_CLAW_SKILL_V01.2024-06-19_CLAW_LOADER_V01")
globals().update({'SkillDef': getattr(m_2024_06_19_CLAW_SKILL_V01_2024_06_19_CLAW_LOADER_V01, 'SkillDef'), 'load_skills': getattr(m_2024_06_19_CLAW_SKILL_V01_2024_06_19_CLAW_LOADER_V01, 'load_skills'), 'find_skill': getattr(m_2024_06_19_CLAW_SKILL_V01_2024_06_19_CLAW_LOADER_V01, 'find_skill'), 'substitute_arguments': getattr(m_2024_06_19_CLAW_SKILL_V01_2024_06_19_CLAW_LOADER_V01, 'substitute_arguments'), '_parse_skill_file': getattr(m_2024_06_19_CLAW_SKILL_V01_2024_06_19_CLAW_LOADER_V01, '_parse_skill_file'), '_parse_list_field': getattr(m_2024_06_19_CLAW_SKILL_V01_2024_06_19_CLAW_LOADER_V01, '_parse_list_field')})
import importlib
m_2024_06_19_CLAW_SKILL_V01_2024_06_19_CLAW_EXECUTOR_V01 = importlib.import_module("2024-06-19_CLAW_SKILL_V01.2024-06-19_CLAW_EXECUTOR_V01")
globals().update({'execute_skill': getattr(m_2024_06_19_CLAW_SKILL_V01_2024_06_19_CLAW_EXECUTOR_V01, 'execute_skill')})

# Legacy constant — kept for tests that patch it
import importlib
m_2024_06_19_CLAW_SKILL_V01_2024_06_19_CLAW_LOADER_V01 = importlib.import_module("2024-06-19_CLAW_SKILL_V01.2024-06-19_CLAW_LOADER_V01")
globals().update({'_gsp': getattr(m_2024_06_19_CLAW_SKILL_V01_2024_06_19_CLAW_LOADER_V01, '_get_skill_paths')})
SKILL_PATHS = _gsp()
