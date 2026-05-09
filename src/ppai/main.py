#!/usr/bin/env python3
"""
PPAI v0.6 - Personal Private AI
Phase 1 Bootstrap - Working Grok Chat (Termux)
"""
print("🚀 PPAI v0.6 - Personal Private AI")
print("====================================")
print("✅ Architecture approved")
print("✅ Lightweight Grok Backend loaded")
print("✅ Your sovereign Wisdom Keeper is online!\n")

from core.grok_backend import GrokBackend
from interfaces.llm_backend import LLMBackend

def main():
    llm: LLMBackend = GrokBackend()
    
    print("Type your message below. Type 'exit' or 'quit' to stop.\n")
    
    messages = [{"role": "system", "content": "You are PPAI, a sovereign Personal Private AI and Wisdom Keeper. Be helpful, truthful, and aligned with human flourishing."}]
    
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("👋 PPAI shutting down. See you soon!")
                break
            
            if not user_input:
                continue
                
            messages.append({"role": "user", "content": user_input})
            
            print("PPAI: ", end="", flush=True)
            response = llm.chat_completion(messages, temperature=0.8)
            print(response)
            
            messages.append({"role": "assistant", "content": response})
            
        except Exception as e:
            print(f"\n⚠️ Error: {e}")
            print("Tip: Double-check your GROK_API_KEY in .env")

if __name__ == "__main__":
    main()
