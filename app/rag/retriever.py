from app.rag.index import create_index

from llama_index.core.vector_stores import (
    MetadataFilters,
    MetadataFilter,
    FilterOperator,
    FilterCondition
)

def get_retriever(index,selected_files=None):
    filters = None 
    if selected_files:
        filters = MetadataFilters(
            filters=[
                MetadataFilter(
                    key="file_name",
                    value=file_name,
                    operator=FilterOperator.EQ
                )
                for file_name in selected_files
            ],
            condition = FilterCondition.OR
            # condition="or" # FilterCondition.OR
        )
    retriever = index.as_retriever(
        similarity_top_k=5,
        filters=filters
    )
    return retriever

# def get_retriever(index):

#     return index.as_retriever(
#         similarity_top_k=5
#     )