from dataclasses import dataclass


@dataclass
class ChatBase:
    """Abstract base class for chat functionality."""

    @classmethod
    def send_message(cls, message: str) -> str:
        """Placeholder method for sending messages."""
        return "Hello from Chat"

    @classmethod
    def receive_message(cls) -> str:
        """Placeholder method for receiving messages."""
        return "Hello from Chat"
