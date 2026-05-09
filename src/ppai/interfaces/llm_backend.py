from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator, Dict, List, Optional

class LLMBackend(ABC):
    """LLM Backend Abstraction Layer - Grok API in Phase 1, local later."""
    @abstractmethod
    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        tools: Optional[List[Dict]] = None,
        tool_choice: Optional[str] = None,
        stream: bool = False,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs: Any,
    ) -> Any:
        pass

    @abstractmethod
    async def get_model_info(self) -> Dict[str, Any]:
        pass
