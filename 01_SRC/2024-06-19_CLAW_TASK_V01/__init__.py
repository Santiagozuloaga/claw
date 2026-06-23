"""Task system for clawspring."""
import importlib; _m_types = importlib.import_module(".2024-06-19_CLAW_TYPES_V01", __package__); globals().update({'Task': getattr(_m_types, 'Task'), 'TaskStatus': getattr(_m_types, 'TaskStatus')})
import importlib; _m_store = importlib.import_module(".2024-06-19_CLAW_STORE_V01", __package__); globals().update({'create_task': getattr(_m_store, 'create_task'), 'get_task': getattr(_m_store, 'get_task'), 'list_tasks': getattr(_m_store, 'list_tasks'), 'update_task': getattr(_m_store, 'update_task'), 'delete_task': getattr(_m_store, 'delete_task'), 'clear_all_tasks': getattr(_m_store, 'clear_all_tasks'), 'reload_from_disk': getattr(_m_store, 'reload_from_disk')})

__all__ = [
    "Task", "TaskStatus",
    "create_task", "get_task", "list_tasks", "update_task",
    "delete_task", "clear_all_tasks", "reload_from_disk",
]
