"""Backward-compatibility shim — real implementation is in memory/ package."""
import importlib; _mod = importlib.import_module('2024-06-19_CLAW_MEMORY_PACKAGE_V01.store'); globals().update({k: getattr(_mod, k) for k in []}) # noqa: F401
    MemoryEntry,
    save_memory,
    delete_memory,
    load_index,
    search_memory,
    get_index_content,
    parse_frontmatter,
)
import importlib; _mod = importlib.import_module('2024-06-19_CLAW_MEMORY_PACKAGE_V01.context'); globals().update({k: getattr(_mod, k) for k in ['get_memory_context']}) # noqa: F401
