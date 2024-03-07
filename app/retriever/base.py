from dataclasses import dataclass


@dataclass
class RetrieverBase:
    """Abstract base class for Retriever"""

    @classmethod
    def meth(cls, prompt_id: str) -> str:
        """Placeholder method for meth."""
        return "Hello from Retriever"