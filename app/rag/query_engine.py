from llama_index.core.query_engine import RetrieverQueryEngine

from app.rag.retriever import get_retriever
from app.core.llm import get_llm

def get_query_engine(index, selected_files=None):

    retriever = get_retriever(
        index=index,
        selected_files=selected_files
    )

    query_engine = RetrieverQueryEngine.from_args(
        retriever=retriever,
        llm=get_llm()
    )

    return query_engine


# def get_query_engine(index):

#     return index.as_query_engine(
#         similarity_top_k=5,
#         llm = get_llm()
#     )