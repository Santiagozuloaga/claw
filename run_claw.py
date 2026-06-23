#!/usr/bin/env python3
import sys
from pathlib import Path
import importlib
project_root = Path(__file__).parent.absolute()
sys.path.insert(0, str(project_root / "01_SRC"))
sys.path.insert(0, str(project_root / "00_SOPORTE"))
core = importlib.import_module("2024-06-19_CLAW_CORE_V01")
if __name__ == "__main__":
    core.main()
