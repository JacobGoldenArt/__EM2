from dataclasses import dataclass


@dataclass
class PromptsBase:
    """Abstract base class for prompt management."""

    @classmethod
    def load_prompt(cls, prompt_id: str) -> str:
        """Placeholder method for loading prompts."""
        return "Hello from Prompts"
