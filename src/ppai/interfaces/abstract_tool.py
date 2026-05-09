from abc import ABC, abstractmethod
from typing import Any, Dict

class AbstractTool(ABC):
    """Every tool must follow this contract (file tools, future robot tools, etc.)."""
    name: str
    description: str

    @abstractmethod
    def get_schema(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def execute(self, parameters: Dict[str, Any]) -> Any:
        pass
