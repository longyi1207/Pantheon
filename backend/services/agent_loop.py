from .llm_interface import LLMInterface
from .client_repository import ClientRepository
from ..prompts.system_prompts import INITIAL_MESSAGE_PROMPT, NEXT_STEP_PROMPT


class AgentLoop:
    """Main agent loop for handling tasks."""

    def __init__(self, llm: LLMInterface, client_repo: ClientRepository):
        self.llm = llm
        self.client_repo = client_repo
        self.messages = [INITIAL_MESSAGE_PROMPT]

    def run(self, user_input: str):
        self.messages.append({"role": "user", "content": user_input})
        for _ in range(10):  # Max iterations
            response = self.llm.chat_completion(self.messages, self.client_repo.clients)
            self.messages.append(response["choices"][0]["message"])
            if response["choices"][0]["finish_reason"] == "stop":
                break
            if "tool_call" in response["choices"][0]["message"]:
                tool_name = response["choices"][0]["message"]["tool_call"]["name"]
                tool_args = response["choices"][0]["message"]["tool_call"]["arguments"]
                client = self.client_repo.get_client(tool_name)
                success, result = client.call_tool(tool_name, tool_args)
                self.messages.append(
                    {
                        "role": "tool",
                        "content": f"Result: {result}" if success else f"Error: {result}",
                    }
                )
            self.messages.append(NEXT_STEP_PROMPT)
