import os
from dotenv import load_dotenv

load_dotenv()

QDRANT_URL = os.getenv(
    "QDRANT_URL",
    "http://localhost:6333"
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "documind_docs"
)

EMBED_MODEL = os.getenv(
    "EMBED_MODEL",
    "BAAI/bge-small-en-v1.5"
)

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "ollama"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2:3b"
)

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434"
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
