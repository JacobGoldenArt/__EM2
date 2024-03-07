from dataclasses import dataclass


@dataclass
class MemoryBase:
    """Abstract base class for Memory"""

    @classmethod
    def meth(cls, prompt_id: str) -> str:
        """Placeholder method for meth."""
        return "Hello from Memory"
