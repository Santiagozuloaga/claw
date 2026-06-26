"""Backward-compatibility shim — real implementation is in skill/ package."""
from CLAW_2024_06_19_CLAW_SKILL_V01.loader import (  # noqa: F401
    SkillDef,
    load_skills,
    find_skill,
    substitute_arguments,
    _parse_skill_file,
    _parse_list_field,
)
from CLAW_2024_06_19_CLAW_SKILL_V01.executor import execute_skill  # noqa: F401

# Legacy constant — kept for tests that patch it
from CLAW_2024_06_19_CLAW_SKILL_V01.loader import _get_skill_paths as _gsp
SKILL_PATHS = _gsp()
