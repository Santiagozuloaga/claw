"""Backward-compatibility shim — real implementation is in skill/ package."""
import importlib; _mod = importlib.import_module('2024-06-19_CLAW_SKILL_V01.loader'); globals().update({k: getattr(_mod, k) for k in []}) # noqa: F401
    SkillDef,
    load_skills,
    find_skill,
    substitute_arguments,
    _parse_skill_file,
    _parse_list_field,
)
import importlib; _mod = importlib.import_module('2024-06-19_CLAW_SKILL_V01.executor'); globals().update({k: getattr(_mod, k) for k in ['execute_skill']}) # noqa: F401

# Legacy constant — kept for tests that patch it
import importlib; _mod = importlib.import_module('2024-06-19_CLAW_SKILL_V01.loader'); globals().update({k: getattr(_mod, k) for k in ['_get_skill_paths as _gsp']})
SKILL_PATHS = _gsp()
