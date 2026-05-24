from llama_index.llms.ollama import Ollama 
from llama_index.llms.openai import OpenAI
from app.core.settings import (OLLAMA_MODEL,OLLAMA_BASE_URL )

def get_llm():
    print("Using model:", OLLAMA_MODEL)
    return Ollama(model = OLLAMA_MODEL, base_url = OLLAMA_BASE_URL,
     request_timeout = 120.0,
     context_window=4096)