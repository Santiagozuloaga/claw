"""skill package — reusable prompt templates (skills)."""
import importlib; _m_loader = importlib.import_module(".2024-06-19_CLAW_LOADER_V01", __package__); globals().update({'SkillDef': getattr(_m_loader, 'SkillDef'), 'load_skills': getattr(_m_loader, 'load_skills'), 'find_skill': getattr(_m_loader, 'find_skill'), 'substitute_arguments': getattr(_m_loader, 'substitute_arguments'), 'register_builtin_skill': getattr(_m_loader, 'register_builtin_skill'), '_parse_skill_file': getattr(_m_loader, '_parse_skill_file'), '_parse_list_field': getattr(_m_loader, '_parse_list_field')})
import importlib; _m_executor = importlib.import_module(".2024-06-19_CLAW_EXECUTOR_V01", __package__); globals().update({'execute_skill': getattr(_m_executor, 'execute_skill')})

# Importing builtin registers the built-in skills
from . import builtin as _builtin  # noqa: F401
