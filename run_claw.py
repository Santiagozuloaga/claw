#!/usr/bin/env python3
import sys
from pathlib import Path
import importlib

# Set paths for P.A.R.A. structure
project_root = Path(__file__).parent.absolute()
sys.path.insert(0, str(project_root / "01_SRC"))
sys.path.insert(0, str(project_root / "00_SOPORTE"))

# Import core
core = importlib.import_module("CLAW_2024_06_19_CORE_V01")

if __name__ == "__main__":
    core.main()
