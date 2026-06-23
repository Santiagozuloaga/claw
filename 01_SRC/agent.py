"""Backward-compatibility shim — real implementation is in the ISO-SAGE
canonical module ``2024-06-19_CLAW_AGENT_CORE_V01.py``.

This short-named module restores the importable ``agent`` module declared in
``pyproject.toml`` (``py-modules``). The canonical implementation lives in the
ISO-SAGE-named file (which cannot be imported as a normal Python module because
its name starts with a digit and contains hyphens). We load it by path and
re-export its public API.

Note: ``2024-06-19_CLAW_AGENT_CORE_V01.py`` is the clean variant (uses short
module names: ``tool_registry``, ``tools``, ``providers``, ``compaction``).
The older ``2024-06-19_CLAW_AGENT_V01.py`` has stale top-level imports
referencing deleted ``CLAW_2024_06_19_*`` modules and is not used here.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_ISO_MODULE = Path(__file__).with_name("2024-06-19_CLAW_AGENT_CORE_V01.py")

_spec = importlib.util.spec_from_file_location("claw_agent_canonical", _ISO_MODULE)
assert _spec is not None and _spec.loader is not None
_canonical = importlib.util.module_from_spec(_spec)
# Register before exec so dataclass/typing can resolve __module__.
sys.modules["claw_agent_canonical"] = _canonical
_spec.loader.exec_module(_canonical)

for _name in dir(_canonical):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_canonical, _name)

__all__ = [n for n in dir(_canonical) if not n.startswith("_")]
