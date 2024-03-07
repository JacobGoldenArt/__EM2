from dataclasses import dataclass


@dataclass
class VoiceBase:
    """Abstract base class for voice input/output."""

    @classmethod
    def voice_in(cls, input: str) -> str:
        """Placeholder method for voice input."""
        return "Hello from Voice Input"

    @classmethod
    def voice_out(cls, output: str) -> None:
        """Placeholder method for voice output."""
        print("Hello from Voice Output")
