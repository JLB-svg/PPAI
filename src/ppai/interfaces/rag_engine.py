from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class RAGEngine(ABC):
    """Wisdom Keeper RAG Engine - personal + historical wisdom indexes."""
    @abstractmethod
    async def ingest_documents(self, documents: List[Dict[str, Any]], index_name: str = "personal") -> None:
        pass

    @abstractmethod
    async def retrieve(self, query: str, top_k: int = 5, index_name: Optional[str] = None) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    async def generate_proactive_insights(self, conversation_context: List[Dict], num_insights: int = 3) -> List[str]:
        pass
