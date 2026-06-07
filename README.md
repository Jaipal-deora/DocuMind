# 🧠 DocuMind - A RAG System 
A local lightweight Retrievel Augment Generation (RAG) system developed using Python and open-source tools. It enhances LLM responses by grounding them in custom data sources, making output more accurate, relevant, and reliable. 

## 🚀 What This Project Does
This system allows you to:
- Ask questions about your own data (PDF files)
- Retrieve relevant context using embeddings 
- LLM generated smart responses 
- Document can be selected for more grounded results in the case of multiple documents

## 🧱 How It Works
1.  Ingestion 
    - Load documents 
    - Split into chunks 

2. Embedding 
    - Convert chunks into vector embeddings 

3. Storage
    - Store embeddings in a vector database (qdrant here)

4. Retrievel 
    - User query - converted into embedding 
    - Top relevant chunks are retrieved 

5. Generation 
    - Retrieved context + query -> passed to LLM 
    - Final grounded response generated 

## 🛠️ Tech Stack
- Python
- LlamaIndex
- Vector DB (Qdrant)
- Embeddings (BAAI/bge-small-en-v1.5)
- LLM (Ollama llama3.2:3b)

## ⚙️ Setup
1. Clone the repo 
2. Install dependencies 
    - pip install -r requirements.txt
3. Run backend 
    - uvicorn app.main:app 
4. Run UI 
    - streamlit run ui.streamlit_app.py
5. Upload data and chat 

## ⚠️ Limitations
- Tested only on PDF files 
- Depends on embedding quality
- Retrieval may miss context if poor chunking 
- Local setup so depends on hardware 
- Requires tuning for best results 

## 🔐 Future Improvements\
- Document normalization
- Better chunking stategies 
- Hybrid search (currently filtered on file is supported)
- Caching respones 
- Evaluation metrics for answer quality
