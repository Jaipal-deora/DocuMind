# from llama_index.embeddings.ollama import OllamaEmbedding 
from llama_index.embeddings.fastembed import FastEmbedEmbedding
from app.core.settings import EMBED_MODEL

# def get_embed_model():
#     return OllamaEmbedding(
#         model_name = os.getenv('OLLAMA_EMBED_MODEL','nomic-embed-text'),
#         base_url = os.getenv("OLLAMA_URL")
#     )

def get_embed_model():
    return FastEmbedEmbedding(
        model_name = EMBED_MODEL
    )

