#!/usr/bin/env python3
# === UTF-8 Windows fix (Bug #4) — ANTES de cualquier import/print ===
import sys as _sys, os as _os
if _sys.platform == "win32":
    ...
# === FIN UTF-8 fix ===
"""
ClawSpring — Minimal Python implementation of Claude Code.
...
"""
from __future__ import annotations