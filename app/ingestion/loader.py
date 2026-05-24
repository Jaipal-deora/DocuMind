from pathlib import Path
from llama_index.core import SimpleDirectoryReader
from app.utils.file_hash import calculate_file_hash

def load_docs(path:str):
    all_docs = []
    for file_path in Path(path).glob("*"):
        if not file_path.is_file():
            continue
        docs = SimpleDirectoryReader(
            input_files=[str(file_path)]
        ).load_data()
        file_hash = calculate_file_hash(str(file_path))
        for doc in docs:
            doc.metadata['file_name'] = file_path.name#str(file_path)
            doc.metadata['file_hash'] = file_hash
        all_docs.extend(docs)
    return all_docs 


# from llama_index.core import SimpleDirectoryReader 

# def load_documents(path:str):
#     documents = SimpleDirectoryReader(
#         input_dir=path
#     ).load_data()
#     return documents
