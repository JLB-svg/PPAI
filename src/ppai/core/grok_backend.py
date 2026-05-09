from interfaces.llm_backend import LLMBackend
import requests
import json
from typing import Any, Dict, List
import os
from dotenv import load_dotenv

load_dotenv()

class GrokBackend(LLMBackend):
    """Phase 1: Lightweight Grok API (supports new xai- keys)."""
    
    def __init__(self):
        self.api_key = os.getenv("GROK_API_KEY", "").strip()
        if not self.api_key.startswith(("xai-", "sk-xai-")):
            raise ValueError("❌ Invalid GROK_API_KEY in .env — must start with xai- or sk-xai-")
        self.model = "grok-4.20-reasoning"   # Current recommended model
        self.base_url = "https://api.x.ai/v1"
        print("✅ New xai- API key loaded successfully!")

    def chat_completion(self, messages: List[Dict[str, str]], temperature: float = 0.7, **kwargs: Any) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            **kwargs
        }
        
        response = requests.post(f"{self.base_url}/chat/completions", headers=headers, json=data, timeout=60)
        
        if response.status_code != 200:
            print(f"\n❌ API Error {response.status_code}:")
            try:
                print(json.dumps(response.json(), indent=2))
            except:
                print(response.text)
            response.raise_for_status()
        
        result = response.json()
        return result["choices"][0]["message"]["content"]

    async def get_model_info(self) -> Dict[str, Any]:
        return {"model": self.model, "provider": "xAI Grok", "status": "connected"}
