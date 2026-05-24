from app.core.vectorstore import get_vector_store

client = None
embed_model = None
vector_store = None

def initialize_vector_store():
    global client 
    global embed_model 
    global vector_store 

    client, embed_model, vector_store = get_vector_store()

def get_client():
    return client

def get_embed_model():
    return embed_model 

def get_vectorstore():
    return vector_store