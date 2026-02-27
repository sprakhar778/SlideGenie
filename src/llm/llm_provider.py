from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

def get_llm(model_name: str = "gemini-3.1-pro-preview", temperature: float = 0.3):
    """Factory function to initialize and return a configured LLM instance."""
    llm = ChatGoogleGenerativeAI(model=model_name, temperature=temperature)
    return llm