
import os 
import qdrant_client 
from llama_index.vector_stores.qdrant import QdrantVectorStore
from app.core.settings  import (QDRANT_URL,COLLECTION_NAME)
from qdrant_client.models import VectorParams, Distance 

from app.core.embedder import get_embed_model 

def get_embedding_dimension(embed_model):
    vector = embed_model.get_text_embedding("test")
    return len(vector)

def ensure_collection(client, collection_name, embed_model):

    if client.collection_exists(collection_name):
        return

    vector_size = get_embedding_dimension(embed_model)

    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=vector_size,
            distance=Distance.COSINE
        )
    )    

def get_vector_store(collection_name = COLLECTION_NAME):
    client = qdrant_client.QdrantClient(url=QDRANT_URL,prefer_grpc=True)

    embed_model = get_embed_model()
    ensure_collection(
        client=client,
        collection_name=collection_name,
        embed_model=embed_model
    )

    return client, embed_model,QdrantVectorStore(client=client,collection_name=collection_name)