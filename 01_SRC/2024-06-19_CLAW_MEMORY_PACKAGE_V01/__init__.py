"""Memory package for clawspring.

Provides persistent, file-based memory across conversations.

Storage layout:
  user scope    : ~/.clawspring/memory/<slug>.md   (shared across projects)
  project scope : .clawspring/memory/<slug>.md     (local to cwd)

The MEMORY.md index in each directory is auto-maintained and injected
into the system prompt so Claude has an overview of available memories.

Public API (backward-compatible with the old memory.py module):
  MemoryEntry      — dataclass for a single memory
  save_memory()    — write/update a memory file
  delete_memory()  — remove a memory file
  load_index()     — load all entries from one or both scopes
  search_memory()  — keyword search across entries
  get_memory_context() — MEMORY.md content for system prompt injection
"""
import importlib; _m_store = importlib.import_module(".2024-06-19_CLAW_STORE_V01", __package__); globals().update({'MemoryEntry': getattr(_m_store, 'MemoryEntry'), 'save_memory': getattr(_m_store, 'save_memory'), 'delete_memory': getattr(_m_store, 'delete_memory'), 'load_index': getattr(_m_store, 'load_index'), 'load_entries': getattr(_m_store, 'load_entries'), 'search_memory': getattr(_m_store, 'search_memory'), 'get_index_content': getattr(_m_store, 'get_index_content'), 'parse_frontmatter': getattr(_m_store, 'parse_frontmatter'), 'USER_MEMORY_DIR': getattr(_m_store, 'USER_MEMORY_DIR'), 'INDEX_FILENAME': getattr(_m_store, 'INDEX_FILENAME'), 'MAX_INDEX_LINES': getattr(_m_store, 'MAX_INDEX_LINES'), 'MAX_INDEX_BYTES': getattr(_m_store, 'MAX_INDEX_BYTES')})
import importlib; _m_scan = importlib.import_module(".2024-06-19_CLAW_SCAN_V01", __package__); globals().update({'MemoryHeader': getattr(_m_scan, 'MemoryHeader'), 'scan_memory_dir': getattr(_m_scan, 'scan_memory_dir'), 'scan_all_memories': getattr(_m_scan, 'scan_all_memories'), 'format_memory_manifest': getattr(_m_scan, 'format_memory_manifest'), 'memory_age_days': getattr(_m_scan, 'memory_age_days'), 'memory_age_str': getattr(_m_scan, 'memory_age_str'), 'memory_freshness_text': getattr(_m_scan, 'memory_freshness_text')})
import importlib; _m_context = importlib.import_module(".2024-06-19_CLAW_CONTEXT_V01", __package__); globals().update({'get_memory_context': getattr(_m_context, 'get_memory_context'), 'find_relevant_memories': getattr(_m_context, 'find_relevant_memories'), 'truncate_index_content': getattr(_m_context, 'truncate_index_content')})
import importlib; _m_types = importlib.import_module(".2024-06-19_CLAW_TYPES_V01", __package__); globals().update({'MEMORY_TYPES': getattr(_m_types, 'MEMORY_TYPES'), 'MEMORY_TYPE_DESCRIPTIONS': getattr(_m_types, 'MEMORY_TYPE_DESCRIPTIONS'), 'MEMORY_SYSTEM_PROMPT': getattr(_m_types, 'MEMORY_SYSTEM_PROMPT'), 'WHAT_NOT_TO_SAVE': getattr(_m_types, 'WHAT_NOT_TO_SAVE')})
import importlib; _m_consolidator = importlib.import_module(".2024-06-19_CLAW_CONSOLIDATOR_V01", __package__); globals().update({'consolidate_session': getattr(_m_consolidator, 'consolidate_session')})

__all__ = [
    # store
    "MemoryEntry",
    "save_memory",
    "delete_memory",
    "load_index",
    "load_entries",
    "search_memory",
    "get_index_content",
    "parse_frontmatter",
    "USER_MEMORY_DIR",
    "INDEX_FILENAME",
    "MAX_INDEX_LINES",
    "MAX_INDEX_BYTES",
    # scan
    "MemoryHeader",
    "scan_memory_dir",
    "scan_all_memories",
    "format_memory_manifest",
    "memory_age_days",
    "memory_age_str",
    "memory_freshness_text",
    # context
    "get_memory_context",
    "find_relevant_memories",
    "truncate_index_content",
    # types
    "MEMORY_TYPES",
    "MEMORY_TYPE_DESCRIPTIONS",
    "MEMORY_SYSTEM_PROMPT",
    "WHAT_NOT_TO_SAVE",
    # consolidator
    "consolidate_session",
]
