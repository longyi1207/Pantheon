from llm.llm_interface import LLMInterface
from mcp_client.client_repository import ClientRepository
from llm.prompts.system_prompts import INITIAL_MESSAGE_PROMPT, NEXT_STEP_PROMPT
from utils.logger import setup_logger
from mcp_server.bash import BashTool
from mcp_client.mcp_client import MCPClient
from mcp_server.base import ToolError, ToolResult, ToolFailure
class AgentLoop:
    """Main agent loop for handling tasks."""

    def __init__(self, llm: LLMInterface, client_repo: ClientRepository):
        self.llm = llm
        self.client_repo = client_repo
        self.messages = []
        self.logger = setup_logger(__name__)

        bashMcpClient = MCPClient(BashTool())
        self.client_repo.add_client("bash", bashMcpClient)
        self.tools = self.client_repo.get_all_tools()

    def run(self, user_input: list[str]) -> list[str]:
        self.logger.info("Starting agent loop with user input: %s", user_input)
        self.messages = user_input
        userInputMsgIdx = len(self.messages)
        for _ in range(10):  # Max iterations
            print("messages", self.messages)
            response = self.llm.chat_completion(self.messages, self.tools.to_params())
            print("response", response)
            message, tools = self.llm.parse_response(response)
            self.logger.debug("Received response: %s", message)
            print("message", message, tools)
            if tools:
                for tool in tools:
                    client = self.client_repo.get_client(tool)
                    #TODO: add args
                    result : ToolError| ToolResult| ToolFailure = client.call_tool(tool, {})
                    self.logger.info("Tool call result: %s", "Success" if isinstance(result, ToolResult) else "Failure")
                    self.messages.append({"role": "user", "content": f"Result of {tool}: {result}" if isinstance(result, ToolResult) else f"Error calling {tool}: {result}"})
            else:
                self.messages.append({"role": "assistant", "content": message[0]})
                break
            # self.messages.append(NEXT_STEP_PROMPT)
            # self.logger.debug("Appended next step prompt.")
        return self.messages[userInputMsgIdx:]