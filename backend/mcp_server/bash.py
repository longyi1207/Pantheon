import asyncio
import os
from typing import ClassVar, Literal

from anthropic.types.beta import BetaToolBash20241022Param

from .base import BaseMCPTool, CLIResult, ToolError, ToolResult


class _BashSession:
    """A session of a bash shell."""

    command: str = "/bin/bash"
    _output_delay: float = 0.2  # seconds
    _timeout: float = 120.0  # seconds
    _sentinel: str = "<<exit>>"

    def __init__(self):
        print("Bash session initialized.")
        self._timed_out = False

    async def run(self, command: str):
        process = await asyncio.create_subprocess_shell(
            self.command ,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        process.stdin.write(command.encode() + b"\n")
        process.stdin.write(f"echo '{self._sentinel}'\n".encode())  # Quote the sentinel
        process.stdin.write(b"exit\n")
        await process.stdin.drain()

        # read output from the process, until the sentinel is found
        try:
            output, error = await asyncio.wait_for(process.communicate(), timeout=self._timeout)
            output = output.decode().strip()
            error = error.decode().strip()

            if self._sentinel in output:
                output = output.replace(self._sentinel, '').strip()

        except asyncio.TimeoutError:
            self._timed_out = True
            raise ToolError(
                f"timed out: bash has not returned in {self._timeout} seconds and must be restarted",
            ) from None

        return CLIResult(output=output, error=error)


class BashTool(BaseMCPTool):
    """
    A tool that allows the agent to run bash commands.
    The tool parameters are defined by Anthropic and are not editable.
    """

    _session: _BashSession | None
    name: ClassVar[Literal["bash"]] = "bash"
    api_type: ClassVar[Literal["bash_20241022"]] = "bash_20241022"

    def __init__(self):
        super().__init__()

    async def __call__(
        self, command: str | None = None, **kwargs
    ):
        self._session = _BashSession()

        if command is not None:
            return await self._session.run(command)

        raise ToolError("no command provided.")

    def to_params(self) -> BetaToolBash20241022Param:
        return {
            "type": self.api_type,
            "name": self.name,
        }