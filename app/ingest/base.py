from dataclasses import dataclass


@dataclass
class IngestBase:
    """Abstract base class for Ingest"""

    @classmethod
    def meth(cls, prompt_id: str) -> str:
        """Placeholder method for meth."""
        return "Hello from Ingest"