from llm.llm_interface import LLMInterface
from mcp_server.collection import ToolCollection
from llm.prompts.system_prompts import INITIAL_MESSAGE_PROMPT, NEXT_STEP_PROMPT
from utils.logger import setup_logger
from mcp_server.base import ToolError, ToolResult, ToolFailure
from typing import List, Any, cast
from llm.llm_interface import BetaToolUseBlockParam

class AgentLoop:
    """Main agent loop for handling tasks."""

    def __init__(self, llm: LLMInterface, tools: ToolCollection):
        self.llm = llm
        self.tools = tools
        self.messages = []
        self.logger = setup_logger(__name__)

    async def run(self, user_input: list[str]) -> list[str]:
        self.logger.info("Starting agent loop with user input: %s", user_input)
        self.messages = user_input
        userInputMsgIdx = len(self.messages)
        for _ in range(10):  # Max iterations
            response = self.llm.chat_completion(self.messages, self.tools.to_params())
            message, tools = self.llm.parse_response(response)
            self.logger.debug("Received response: %s", message)

            if tools:
                for tool in tools:
                    tool_name = tool['name']
                    tool_input=cast(dict[str, Any], tool["input"])
                   
                    result = await self.tools.run(
                        name=tool_name,
                        tool_input=tool_input,
                    )

                    self.logger.info("Tool call result: %s", "Success" if isinstance(result, ToolResult) else "Failure")
                    self.messages.append({"role": "user", "content": f"Result of {tool}: {result}" if isinstance(result, ToolResult) else f"Error calling {tool}: {result}"})
            else:
                self.messages.append({"role": "assistant", "content": message[0]})
                break
            # self.messages.append(NEXT_STEP_PROMPT)
            # self.logger.debug("Appended next step prompt.")
        return self.messages[userInputMsgIdx:]