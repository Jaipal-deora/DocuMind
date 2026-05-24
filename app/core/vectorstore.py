
import os 
import qdrant_client 
from llama_index.vector_stores.qdrant import QdrantVectorStore
from app.core.settings  import (QDRANT_URL,COLLECTION_NAME)

def get_vector_store(collection_name = COLLECTION_NAME):
    client = qdrant_client.QdrantClient(url=QDRANT_URL,prefer_grpc=True)
    return QdrantVectorStore(client=client,collection_name=collection_name)