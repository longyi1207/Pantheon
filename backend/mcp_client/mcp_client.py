from typing import Tuple, Any, Dict
from mcp_server.base import BaseMCPTool

class MCPClient:
    """MCP client to call tools on an MCP server."""

    def __init__(self, tool: BaseMCPTool):
        self.tool = tool

    def call_tool(self, tool_name: str, args: Dict[str, Any]) -> Tuple[bool, Any]:
        return self.tool(args)
    
    def get_tool(self) -> BaseMCPTool:
        return self.tool
