# from typing import Dict, List
# from .mcp_client import MCPClient
# from mcp_server.collection import ToolCollection
# from mcp_server.base import BaseMCPTool

# class ClientRepository:
#     """Repository to manage MCP clients."""

#     def __init__(self):
#         self.clients: Dict[str, MCPClient] = {}

#     def add_client(self, name: str, client: MCPClient):
#         """Add an MCP client."""
#         self.clients[name] = client

#     def get_client(self, name: str) -> MCPClient:
#         """Retrieve an MCP client."""
#         if name not in self.clients:
#             raise ValueError(f"Client {name} not found")
#         return self.clients[name]

#     def get_all_tools(self) -> ToolCollection:
#         """Retrieve all MCP tools."""
#         tools: List[BaseMCPTool] = [    ]
#         for client in self.clients.values():
#             tools.append(client.get_tool())
#         return ToolCollection(tools)