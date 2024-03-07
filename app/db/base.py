from dataclasses import dataclass


@dataclass
class DBBase:
    """Abstract base class for DB"""

    @classmethod
    def meth(cls, prompt_id: str) -> str:
        """Placeholder method for meth."""
        return "Hello from DB"