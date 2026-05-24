from app.ingestion.loader import (
    load_docs
)

from app.ingestion.parser import (
    parse_documents
)

from app.rag.index import (
    create_index
)

from app.core.qdrant_utils import (
    file_already_indexed,
    delete_existing_file
)


def ingest_pipeline(path:str):
    documents = load_docs(path)

    new_docs = []

    for doc in documents:
        file_name = doc.metadata['file_name']
        file_hash = doc.metadata['file_hash']

        if not file_already_indexed(file_name, file_hash):
            delete_existing_file(file_name)
            new_docs.append(doc)
        
        
        if not new_docs:
            print("No new or modified documents found.")
            return None

    nodes = parse_documents(new_docs)
    index = create_index(nodes)
    # return index 


# def ingest_pipeline(path: str):

#     documents = load_documents(path)

#     nodes = parse_documents(documents)

#     index = create_index(nodes)

#     return index