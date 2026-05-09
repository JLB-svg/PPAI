from abc import ABC, abstractmethod
from typing import Any, Dict, List

class PersistenceLayer(ABC):
    """Handles conversation history, backups, and audit logs."""
    @abstractmethod
    async def save_conversation(self, conversation_id: str, messages: List[Dict]) -> None: ...
    @abstractmethod
    async def load_conversation(self, conversation_id: str) -> List[Dict]: ...
    @abstractmethod
    async def create_file_backup(self, file_path: str, content: str) -> str: ...
