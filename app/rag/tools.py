from llama_index.core.tools import (
    FunctionTool
)

from app.rag.query_engine import (
    get_query_engine
)


def build_search_tool(index, selected_files=None):

    query_engine = get_query_engine(index,selected_files)

    def search_documents(query: str):

        response = query_engine.query(query)

        return str(response)

    tool = FunctionTool.from_defaults(
        fn=search_documents,
        name="document_search",
        description=(
            "Search uploaded study documents"
        )
    )

    return tool