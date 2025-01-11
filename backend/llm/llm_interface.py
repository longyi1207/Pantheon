from abc import ABC, abstractmethod
from typing import List, Dict, Any, Tuple, Union
from anthropic import Anthropic
import openai
from anthropic.types.beta import (
    BetaCacheControlEphemeralParam,
    BetaContentBlockParam,
    BetaImageBlockParam,
    BetaMessage,
    BetaMessageParam,
    BetaTextBlock,
    BetaTextBlockParam,
    BetaToolResultBlockParam,
    BetaToolUseBlockParam,
)
from typing import cast

class LLMInterface(ABC):
    """Abstract interface for integrating LLMs like OpenAI, Claude, etc."""

    @abstractmethod
    def chat_completion(
        self, messages: List[Dict[str, str]], tools: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Generate chat completion using the LLM."""
        pass

    @abstractmethod
    def parse_response(self, response: Dict[str, Any]) -> Tuple[List[str], List[str]]:
        """Parse the response from the LLM."""
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
    def parse_response(self, response: Dict[str, Any]) -> Tuple[List[str], List[str]]:
        return response

class ClaudeInterface(LLMInterface):
    """Implementation of the LLMInterface for Claude."""

    def __init__(self, api_key: str, model: str):
        self.client = Anthropic()
        self.client.api_key = api_key
        self.model = model

    def chat_completion(
        self, messages: List[Dict[str, str]], tools: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        response = self.client.beta.messages.with_raw_response.create(
            model=self.model,
            max_tokens=1024,    
            tools=tools,
            messages=messages,
            betas=["computer-use-2024-10-22"],
        )
        return response.parse()
    
    def parse_response(self, response: Dict[str, Any]) -> Tuple[List[str], List[str]]:
        response_params = _response_to_params(response)
        tools_content: List[str] = []
        message_content: List[str] = []
        for content_block in response_params:
            if content_block["type"] == "tool_use":
                tools_content.append(content_block["name"])
            elif content_block["type"] == "text":
                message_content.append(content_block["text"])

        return message_content, tools_content
    
class TestInterface(LLMInterface):
    def chat_completion(self, messages: List[Dict[str, str]], tools: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {"role": "assistant", "content": "This is a test response."}
    
    def parse_response(self, response: Dict[str, Any]) -> Tuple[List[str], List[str]]:
        return response


def _response_to_params(
    response: BetaMessage,
) -> list[Union[BetaTextBlockParam, BetaToolUseBlockParam]]:
    res: list[Union[BetaTextBlockParam, BetaToolUseBlockParam]] = []
    for block in response.content:
        if isinstance(block, BetaTextBlock):
            res.append({"type": "text", "text": block.text})
        elif hasattr(block, 'model_dump') and callable(getattr(block, 'model_dump')):
            res.append(cast(BetaToolUseBlockParam, block.model_dump()))
        else:
            # Handle unexpected block types
            print(f"Unexpected block type: {type(block)}")
    return res
