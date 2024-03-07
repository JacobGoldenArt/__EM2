from dataclasses import dataclass


@dataclass
class CLIBase:
    """Abstract base class for CLI"""

    @classmethod
    def meth(cls, prompt_id: str) -> str:
        """Placeholder method for meth."""
        return "Hello from CLI"