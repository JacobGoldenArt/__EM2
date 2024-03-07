from dataclasses import dataclass


@dataclass
class EmbeddingsBase:
    """Abstract base class for Embeddings"""

    @classmethod
    def meth(cls, prompt_id: str) -> str:
        """Placeholder method for meth."""
        return "Hello from Embeddings"
