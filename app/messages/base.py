from dataclasses import dataclass


@dataclass
class MessagesBase:
    """Abstract base class for Messages"""

    @classmethod
    def meth(cls, prompt_id: str) -> str:
        """Placeholder method for meth."""
        return "Hello from Messages"