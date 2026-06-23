"""mcp package — Model Context Protocol client for clawspring.

Usage
-----
MCP servers are configured in one of two JSON files:

  ~/.clawspring/mcp.json        (user-level, all projects)
  .mcp.json                      (project-level, current dir, overrides user)

Format:
    {
      "mcpServers": {
        "my-git-server": {
          "type": "stdio",
          "command": "uvx",
          "args": ["mcp-server-git"]
        },
        "my-remote": {
          "type": "sse",
          "url": "http://localhost:8080/sse"
        }
      }
    }

Supported transports:
  stdio  — spawn a local subprocess (most common)
  sse    — HTTP Server-Sent Events stream
  http   — plain HTTP POST (Streamable HTTP transport)

MCP tools are automatically discovered on startup and registered into the
tool_registry under the name  mcp__<server>__<tool>.
Claude can invoke them just like built-in tools.
"""
import importlib; _m_types = importlib.import_module(".2024-06-19_CLAW_TYPES_V01", __package__); globals().update({'MCPServerConfig': getattr(_m_types, 'MCPServerConfig'), 'MCPTool': getattr(_m_types, 'MCPTool'), 'MCPServerState': getattr(_m_types, 'MCPServerState'), 'MCPTransport': getattr(_m_types, 'MCPTransport')})
import importlib; _m_client = importlib.import_module(".2024-06-19_CLAW_CLIENT_V01", __package__); globals().update({'MCPClient': getattr(_m_client, 'MCPClient'), 'MCPManager': getattr(_m_client, 'MCPManager'), 'get_mcp_manager': getattr(_m_client, 'get_mcp_manager')})
import importlib; _m_config = importlib.import_module(".2024-06-19_CLAW_CONFIG_V01", __package__); globals().update({'load_mcp_configs': getattr(_m_config, 'load_mcp_configs'), 'save_user_mcp_config': getattr(_m_config, 'save_user_mcp_config'), 'add_server_to_user_config': getattr(_m_config, 'add_server_to_user_config'), 'remove_server_from_user_config': getattr(_m_config, 'remove_server_from_user_config'), 'list_config_files': getattr(_m_config, 'list_config_files')})
import importlib; _m_tools = importlib.import_module(".2024-06-19_CLAW_TOOLS_V01", __package__); globals().update({'initialize_mcp': getattr(_m_tools, 'initialize_mcp'), 'reload_mcp': getattr(_m_tools, 'reload_mcp'), 'refresh_server': getattr(_m_tools, 'refresh_server')})
