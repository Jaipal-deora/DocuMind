import hashlib 
from pathlib import Path 

def calculate_file_hash(file_path: str) -> str:
    hasher = hashlib.md5()

    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)

    return hasher.hexdigest()