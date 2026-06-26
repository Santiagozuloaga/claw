"""Backward-compatibility shim — real implementation is in memory/ package."""
from CLAW_2026_06_24_MEMORY_PACKAGE_V01.store import (  # noqa: F401
    MemoryEntry,
    save_memory,
    delete_memory,
    load_index,
    search_memory,
    get_index_content,
    parse_frontmatter,
)
from CLAW_2026_06_24_MEMORY_PACKAGE_V01.context import get_memory_context  # noqa: F401
