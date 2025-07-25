# ai_agent/services.py

class AIAgentService:
    def __init__(self):
        # Initialize tools or models here if needed
        pass

    def process_message(self, message: str) -> str:
        # For now, just echo the message
        # Later, integrate LangChain, Firecrawl, etc.
        return f"AI Response: {message}"
