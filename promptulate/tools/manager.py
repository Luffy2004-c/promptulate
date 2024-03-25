import inspect
import json
from typing import Any, List, Optional, Union

from promptulate.schema import TOOL_TYPES
from promptulate.tools.base import BaseTool, Tool, ToolImpl, function_to_tool
from promptulate.tools.langchain.tools import LangchainTool


def _judge_langchain_tool_and_wrap(tool: Any) -> Optional[Tool]:
    """Judge if the tool is a langchain tool and wrap it.

    Args:
        tool(Any): The tool to be judged.

    Returns:
        Optional[Tool]: The wrapped tool or None if not a langchain tool.
    """
    try:
        from langchain.tools.base import BaseTool as LangchainBaseTool

        if isinstance(tool, LangchainBaseTool):
            return LangchainTool(tool)

    except ImportError:
        raise ValueError(
            (
                f"Error tool type {tool}, please check the tool type.",
                "If you are using langchain tool, please install -U langchain.",
            )
        )


def _initialize_tool(tool: TOOL_TYPES) -> Optional[Tool]:
    """Initialize the tool.

    Args:
        tool(Union[BaseTool, Callable, Tool, "LangchainBaseToolType"]): The tool to be
            initialized.

    Returns:
        Optional[Tool]: The initialized tool.
    """
    if isinstance(tool, BaseTool):
        return ToolImpl.from_base_tool(tool)
    elif isinstance(tool, Tool):
        return tool
    elif inspect.isfunction(tool):
        return function_to_tool(tool)

    return _judge_langchain_tool_and_wrap(tool)


class ToolManager:
    """ToolManager helps Agent to manage tools"""

    def __init__(self, tools: List[TOOL_TYPES]):
        self.tools: List[Tool] = [
            _initialize_tool(tool)
            for tool in tools
            if _initialize_tool(tool) is not None
        ]

    def get_tool(self, tool_name: str) -> Optional[Tool]:
        """Find specified tool by tool name.
        Args:
            tool_name(str): The name of the tool.

        Returns:
            Optional[Tool]: The specified tool or None if not found.
        """
        return next((tool for tool in self.tools if tool.name == tool_name), None)

    def run_tool(self, tool_name: str, parameters: Union[str, dict]) -> str:
        """Run tool by input tool name and data inputs

        Args:
            tool_name(str): The name of the tool.
            parameters(Union[str, dict]): The parameters for the tool.

        Returns:
            str: The result of the tool.
        """
        tool = self.get_tool(tool_name)

        if tool is None:
            return (
                f"{tool_name} has not been provided yet, please use the provided tool."
            )

        if isinstance(parameters, dict):
            return tool.run(**parameters)
        else:
            return tool.run(parameters)

    @property
    def tool_names(self) -> str:
        """Get all tool names."""
        tool_names = ""
        for tool in self.tools:
            tool_names += f"{tool.name}, "
        return tool_names[:-2]

    @property
    def tool_descriptions(self) -> str:
        """Get all tool descriptions, including the schema if available."""
        tool_descriptions = ""
        for tool in self.tools:
            tool_descriptions += json.dumps(tool.to_schema()) + "\n"
        return tool_descriptions
