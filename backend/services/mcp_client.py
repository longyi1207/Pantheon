from typing import Tuple, Any
import requests
from typing import Dict

class MCPClient:
    """MCP client to call tools on an MCP server."""

    def __init__(self, server_url: str):
        self.server_url = server_url

    def call_tool(self, tool_name: str, args: Dict[str, Any]) -> Tuple[bool, Any]:
        """Calls a tool on the MCP server."""
        try:
            response = requests.post(
                f"{self.server_url}/call-tool",
                json={"name": tool_name, "arguments": args},
            )
            response.raise_for_status()
            return True, response.json()
        except requests.RequestException as e:
            return False, str(e)
