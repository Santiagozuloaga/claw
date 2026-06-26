"""skill package — reusable prompt templates (skills)."""
from CLAW_2026_06_24_SKILL_V01.loader import (  # noqa: F401
    SkillDef,
    load_skills,
    find_skill,
    substitute_arguments,
    register_builtin_skill,
    _parse_skill_file,
    _parse_list_field,
)
from CLAW_2026_06_24_SKILL_V01.executor import execute_skill  # noqa: F401

# Importing builtin registers the built-in skills
from . import builtin as _builtin  # noqa: F401
