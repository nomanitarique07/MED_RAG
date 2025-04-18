# config.py

import os

LLM_CONFIG = {
    "model": "llama3.1",
    "max_tokens": 500,
    "top_p": 0.5,
    "top_k": 5,
    "temperature": 0.1,
    "token_key": os.getenv("OLLAMA_TOKEN", "your-default-token")
}

VECTORDB_CONFIG = {
    "host": "localhost",
    "port": "19530",
    "collection_name": "rag_data",
    "dim": 1024, 
    "metric_type": "L2"
}

EMBEDDING_MODEL = "thenlper/gte-large"

TEMP_DIR = "./tmp_files"
DB_DIR = "./chroma_langchain_db"

os.makedirs(TEMP_DIR, exist_ok=True)