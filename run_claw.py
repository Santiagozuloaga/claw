#!/usr/bin/env python3
import sys
from pathlib import Path
import importlib.util

# Set paths for P.A.R.A. structure
project_root = Path(__file__).parent.absolute()
sys.path.insert(0, str(project_root / "01_SRC"))
sys.path.insert(0, str(project_root / "00_SOPORTE"))

# Import core
# The canonical core module lives in the ISO-SAGE-named file
# `2024-06-19_CLAW_CORE_V01.py`, whose name cannot be used as a Python
# module identifier (starts with a digit, contains hyphens). Load it by path.
_core_path = project_root / "01_SRC" / "2024-06-19_CLAW_CORE_V01.py"
_spec = importlib.util.spec_from_file_location("claw_core", _core_path)
assert _spec is not None and _spec.loader is not None
core = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(core)

if __name__ == "__main__":
    core.main()
