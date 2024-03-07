from dataclasses import dataclass


@dataclass
class BrainBase:
    """Abstract base class for Brain"""

    @classmethod
    def meth(cls, prompt_id: str) -> str:
        """Placeholder method for meth."""
        return "Hello from Brain"