from dataclasses import dataclass


@dataclass
class ToolsBase:
    """Abstract base class for Tools"""

    @classmethod
    def meth(cls, prompt_id: str) -> str:
        """Placeholder method for meth."""
        return "Hello from Tools"
