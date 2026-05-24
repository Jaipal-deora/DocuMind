from llama_index.core import (
    VectorStoreIndex,
    StorageContext
)

from app.rag.core import (
    get_vectorstore,
    get_embed_model
)


def create_index(nodes):

    vector_store = get_vectorstore()

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    index = VectorStoreIndex(
        nodes,
        storage_context=storage_context,
        embed_model=get_embed_model(),
    )

    return index