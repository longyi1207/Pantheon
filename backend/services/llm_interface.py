from abc import ABC, abstractmethod
from typing import List, Dict, Any
import anthropic
import openai

class LLMInterface(ABC):
    """Abstract interface for integrating LLMs like OpenAI, Claude, etc."""

    @abstractmethod
    def chat_completion(
        self, messages: List[Dict[str, str]], tools: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Generate chat completion using the LLM."""
        pass


class OpenAIInterface(LLMInterface):
    """Implementation of the LLMInterface for OpenAI."""

    def __init__(self, api_key: str, model: str):

        self.api_key = api_key
        self.model = model
        openai.api_key = api_key

    def chat_completion(
        self, messages: List[Dict[str, str]], tools: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        import openai
        response = openai.ChatCompletion.create(
            model=self.model,
            temperature=0.2,
            messages=messages,
            tools=tools,
        )
        return response


class ClaudeInterface(LLMInterface):
    """Implementation of the LLMInterface for Claude."""

    def __init__(self, api_key: str):
        self.client = anthropic.Client(api_key)

    def chat_completion(
        self, messages: List[Dict[str, str]], tools: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        response = self.client.completions.create(
            model="claude-3",
            max_tokens=1024,
            temperature=0.2,
            messages=messages,
            tools=tools,
        )
        return response

class TestInterface(LLMInterface):
    def chat_completion(self, messages: List[Dict[str, str]], tools: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {"role": "assistant", "content": "This is a test response."}