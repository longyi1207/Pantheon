from typing import Dict
from .mcp_client import MCPClient


class ClientRepository:
    """Repository to manage MCP clients."""

    def __init__(self):
        self.clients: Dict[str, MCPClient] = {}

    def add_client(self, name: str, client: MCPClient):
        """Add an MCP client."""
        self.clients[name] = client

    def get_client(self, name: str) -> MCPClient:
        """Retrieve an MCP client."""
        if name not in self.clients:
            raise ValueError(f"Client {name} not found")
        return self.clients[name]

    def get_all_clients(self) -> Dict[str, MCPClient]:
        """Retrieve all MCP clients."""
        return self.clients
