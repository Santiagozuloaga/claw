"""Plugin system for clawspring."""
import importlib; _m_types = importlib.import_module(".2024-06-19_CLAW_TYPES_V01", __package__); globals().update({'PluginManifest': getattr(_m_types, 'PluginManifest'), 'PluginEntry': getattr(_m_types, 'PluginEntry'), 'PluginScope': getattr(_m_types, 'PluginScope'), 'parse_plugin_identifier': getattr(_m_types, 'parse_plugin_identifier')})
import importlib; _m_store = importlib.import_module(".2024-06-19_CLAW_STORE_V01", __package__); globals().update({'install_plugin': getattr(_m_store, 'install_plugin'), 'uninstall_plugin': getattr(_m_store, 'uninstall_plugin'), 'enable_plugin': getattr(_m_store, 'enable_plugin'), 'disable_plugin': getattr(_m_store, 'disable_plugin'), 'disable_all_plugins': getattr(_m_store, 'disable_all_plugins'), 'update_plugin': getattr(_m_store, 'update_plugin'), 'list_plugins': getattr(_m_store, 'list_plugins'), 'get_plugin': getattr(_m_store, 'get_plugin')})
import importlib; _m_loader = importlib.import_module(".2024-06-19_CLAW_LOADER_V01", __package__); globals().update({'load_all_plugins': getattr(_m_loader, 'load_all_plugins'), 'load_plugin_tools': getattr(_m_loader, 'load_plugin_tools'), 'load_plugin_skills': getattr(_m_loader, 'load_plugin_skills'), 'load_plugin_mcp_configs': getattr(_m_loader, 'load_plugin_mcp_configs'), 'register_plugin_tools': getattr(_m_loader, 'register_plugin_tools')})
import importlib; _m_recommend = importlib.import_module(".2024-06-19_CLAW_RECOMMEND_V01", __package__); globals().update({'recommend_plugins': getattr(_m_recommend, 'recommend_plugins'), 'recommend_from_files': getattr(_m_recommend, 'recommend_from_files'), 'format_recommendations': getattr(_m_recommend, 'format_recommendations')})

__all__ = [
    "PluginManifest", "PluginEntry", "PluginScope", "parse_plugin_identifier",
    "install_plugin", "uninstall_plugin",
    "enable_plugin", "disable_plugin", "disable_all_plugins",
    "update_plugin", "list_plugins", "get_plugin",
    "load_all_plugins", "load_plugin_tools", "load_plugin_skills",
    "load_plugin_mcp_configs", "register_plugin_tools",
    "recommend_plugins", "recommend_from_files", "format_recommendations",
]
