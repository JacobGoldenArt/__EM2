from dataclasses import dataclass


@dataclass
class APIBase:
    """Abstract base class for external API integration."""

    @classmethod
    def call_api(cls, endpoint: str, params: dict) -> dict:
        """Placeholder method for API calls."""
        return {"message": "Hello from API"}
