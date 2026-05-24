from qdrant_client.models import (
    Filter, FieldCondition, MatchValue,
    FilterSelector
)

from app.rag.core import get_vectorstore


def file_already_indexed(file_name: str, file_hash: str):

    vector_store = get_vectorstore()
    client = vector_store.client
    collection = vector_store.collection_name

    result = client.scroll(
        collection_name=collection,
        limit=1000,
        with_payload=True,
        with_vectors=False
    )

    points = result[0]

    for point in points:

        payload = point.payload or {}

        # CASE 1: flat structure
        if payload.get("file_name") == file_name:
            return payload.get("file_hash") == file_hash

        # CASE 2: nested structure (LlamaIndex style)
        metadata = payload.get("metadata", {})
        if metadata.get("file_name") == file_name:
            return metadata.get("file_hash") == file_hash

    return False

# def file_already_indexed(file_name: str, file_hash: str):

#     vector_store = get_vectorstore()

#     client = vector_store.client
#     collection = vector_store.collection_name

#     result = client.scroll(
#         collection_name=collection,
#         scroll_filter=Filter(
#             must=[
#                 FieldCondition(
#                     key="metadata.file_name",
#                     match=MatchValue(value=file_name)
#                 )
#             ]
#         ),
#         limit=1,
#         with_payload=True
#     )

#     points = result[0]

#     if not points:
#         return False

#     stored_hash = (
#         points[0]
#         .payload
#         .get("metadata", {})
#         .get("file_hash")
#     )

#     return stored_hash == file_hash

def delete_existing_file(file_name: str):

    vector_store = get_vectorstore()

    client = vector_store.client
    collection = vector_store.collection_name

    client.delete(
        collection_name=collection,
        points_selector=FilterSelector(
            filter=Filter(
                should=[   # IMPORTANT: use OR logic
                    FieldCondition(
                        key="file_name",
                        match=MatchValue(value=file_name)
                    ),
                    FieldCondition(
                        key="metadata.file_name",
                        match=MatchValue(value=file_name)
                    )
                ]
                # must=[
                #     FieldCondition(
                #         key="file_name", # metadata.
                #         match=MatchValue(value=file_name)
                #     )
                # ]
            )
        )
    )

    # client.delete(
    #     collection_name=collection,
    #     points_selector={
    #         "filter": {
    #             "must": [
    #                 {
    #                     "key": "metadata.file_name",
    #                     "match": {
    #                         "value": file_name
    #                     }
    #                 }
    #             ]
    #         }
    #     }
    # )

def get_all_indexed_files():
    print('get_all_indexed_files')
    vector_store = get_vectorstore()

    client = vector_store.client
    collection = vector_store.collection_name

    result = client.scroll(
        collection_name=collection,
        limit=10000,
        with_payload=True,
        with_vectors=False
    )

    print(result[0])
    points = result[0]

    files = set()

    for point in points:

        payload = point.payload or {}

        # Case 1: nested metadata
        if "metadata" in payload:
            file_name = payload["metadata"].get("file_name")

        # Case 2: flat structure
        else:
            file_name = payload.get("file_name")

        if file_name:
            files.add(file_name)

    return sorted(files)