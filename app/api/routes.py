from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Query
)

import shutil

from app.ingestion.pipeline import (
    ingest_pipeline
)

from app.agents.study_agent import (
    create_agent
)

from app.rag.query_engine import get_query_engine

from app.core import state 
from app.core.qdrant_utils import get_all_indexed_files
from app.rag.load_index import load_existing_index

router = APIRouter()

# global_index = None
# global_agent = None


@router.get('/documents')
async def get_docs():
    files = get_all_indexed_files()
    # print(files)
    return {"docs": files}
    # return {"docs": "json"}


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    path = f"./data/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # global global_index
    # global global_agent
    #state.index = 
    ingest_pipeline("./data")
    state.index = load_existing_index()
    state.query_engine = get_query_engine(
        state.index
    )
    state.agent = create_agent(
        state.index
    )


    # global_index = ingest_pipeline("./data")

    # global_agent = create_agent(global_index)

    return {
        "message": "Document uploaded"
    }


@router.post("/chat")
async def chat(query: str, selected_files: list[str] = Query(default=[])):

    try:

        if state.index is None:

            return {
                "error": "No indexed documents found"
            }

        query_engine = get_query_engine(
            index=state.index,
            selected_files=selected_files)

        response = query_engine.query(query)
        # response = await state.agent.run(query)

        return {
            "response": str(response)
        }

    except Exception as e:

        return {
            "error": str(e)
        }
