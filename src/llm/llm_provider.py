
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

def get_llm(model_name: str = "openai/gpt-oss-120b", temperature: float = 0.3, streaming: bool = True):
    # model_name="qwen/qwen3-32b"
  
    # model_name="moonshotai/kimi-k2-instruct-0905"
    # model_name="llama-3.3-70b-versatile"
    llm=ChatGroq(model=model_name, temperature=temperature, streaming=streaming, max_tokens=7000, max_retries=5)
    return llm

# def get_llm(model_name: str = "gpt-4o", temperature: float = 0.3, streaming: bool = True):
#     """Factory function to initialize and return a configured LLM instance."""
#     llm = ChatOpenAI(model=model_name, temperature=temperature,streaming=streaming)
#     return llm

# def get_llm(model_name: str = "gemini-3.1-flash-lite-preview", temperature: float = 0.3, streaming: bool = True):
#     """Factory function to initialize and return a configured LLM instance."""
#     # model_name = "gemini-3-flash-preview"
#     # model_name = "gemini-2.5-flash-lite"
#     # model_name="gemini-3.1-pro-preview"
#     # model_name="gemini-3.1-flash-lite-preview"
#     # model_name="gemini-2.5-flash"
#     llm = ChatGoogleGenerativeAI(model=model_name, temperature=temperature,streaming=streaming)
#     # thinking_level="low"
#     return llm