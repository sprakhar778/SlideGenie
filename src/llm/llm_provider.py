from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

# def get_llm(model_name: str = "openai/gpt-oss-120b", temperature: float = 0.3, streaming: bool = True):
#     model_name="qwen/qwen3-32b"
#     llm=ChatGroq(model=model_name, temperature=temperature,streaming=streaming, max_tokens=12000)
#     return llm

# def get_llm(model_name: str = "gpt-4o", temperature: float = 0.3, streaming: bool = True):
#     """Factory function to initialize and return a configured LLM instance."""
#     llm = ChatOpenAI(model=model_name, temperature=temperature,streaming=streaming)
#     return llm

def get_llm(model_name: str = "gemini-3.1-pro-preview", temperature: float = 0.3, streaming: bool = True):
    """Factory function to initialize and return a configured LLM instance."""
    llm = ChatGoogleGenerativeAI(model=model_name, temperature=temperature,streaming=streaming,thinking_level="low")
    return llm