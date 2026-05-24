from app.rag.load_index import load_existing_index
from app.rag.query_engine import get_query_engine
from app.agents.study_agent import (
    create_agent
)

from app.core import state

from app.rag.core import initialize_vector_store


def initialize_rag():

    try:
        initialize_vector_store()
        index = load_existing_index()

        state.index = index

        state.query_engine = get_query_engine(
            index
        )

        state.agent = create_agent(
            index
        )

        print("RAG initialized.")

    except Exception as e:

        print(f"Initialization failed: {e}")

        state.index = None
        state.query_engine = None
        state.agent = None