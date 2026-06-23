"""Backward-compatibility shim — real implementation is in memory/ package."""
import importlib
m_2024_06_19_CLAW_MEMORY_PACKAGE_V01_2024_06_19_CLAW_STORE_V01 = importlib.import_module("2024-06-19_CLAW_MEMORY_PACKAGE_V01.2024-06-19_CLAW_STORE_V01")
globals().update({'MemoryEntry': getattr(m_2024_06_19_CLAW_MEMORY_PACKAGE_V01_2024_06_19_CLAW_STORE_V01, 'MemoryEntry'), 'save_memory': getattr(m_2024_06_19_CLAW_MEMORY_PACKAGE_V01_2024_06_19_CLAW_STORE_V01, 'save_memory'), 'delete_memory': getattr(m_2024_06_19_CLAW_MEMORY_PACKAGE_V01_2024_06_19_CLAW_STORE_V01, 'delete_memory'), 'load_index': getattr(m_2024_06_19_CLAW_MEMORY_PACKAGE_V01_2024_06_19_CLAW_STORE_V01, 'load_index'), 'search_memory': getattr(m_2024_06_19_CLAW_MEMORY_PACKAGE_V01_2024_06_19_CLAW_STORE_V01, 'search_memory'), 'get_index_content': getattr(m_2024_06_19_CLAW_MEMORY_PACKAGE_V01_2024_06_19_CLAW_STORE_V01, 'get_index_content'), 'parse_frontmatter': getattr(m_2024_06_19_CLAW_MEMORY_PACKAGE_V01_2024_06_19_CLAW_STORE_V01, 'parse_frontmatter')})
import importlib
m_2024_06_19_CLAW_MEMORY_PACKAGE_V01_2024_06_19_CLAW_CONTEXT_V01 = importlib.import_module("2024-06-19_CLAW_MEMORY_PACKAGE_V01.2024-06-19_CLAW_CONTEXT_V01")
globals().update({'get_memory_context': getattr(m_2024_06_19_CLAW_MEMORY_PACKAGE_V01_2024_06_19_CLAW_CONTEXT_V01, 'get_memory_context')})
