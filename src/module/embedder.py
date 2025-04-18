from pymilvus import Collection, MilvusException, connections, db, utility
from langchain_milvus import BM25BuiltInFunction, Milvus
from sentence_transformers import SentenceTransformer
from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType
from config import EMBEDDING_MODEL, VECTORDB_CONFIG, DB_DIR
from uuid import uuid4
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings

def embed_and_store(text_chunks):
    conn = connections.connect(host="127.0.0.1", port=19530)
    db_name = "milvus_demo"

    if db_name not in db.list_database():
        db.create_database(db_name)
        print(f"Database '{db_name}' created successfully.")
    db.using_database(db_name)

    URI = "http://localhost:19530"
    embedding_model = OllamaEmbeddings(model="llama3")

    # Initialize vector store with drop_old=True only on first call or conditionally
    vectorstore = Milvus(
        embedding_function=embedding_model,
        collection_name="rag_data",
        connection_args={"uri": URI, "token": "root:Milvus", "db_name": "milvus_demo"},
        index_params={"index_type": "FLAT", "metric_type": "L2"},
        consistency_level="Strong",
        drop_old=False,  # Important!
    )

    # Skip if already populated
    if utility.has_collection("rag_data"):
        print("Collection 'rag_data' already exists. Skipping embedding.")
        return vectorstore

    documents = [Document(str(chunk.page_content)) for chunk in text_chunks]
    uuids = [str(uuid4()) for _ in documents]
    vectorstore.add_documents(documents=documents, ids=uuids)

    return vectorstore

# vectorstore_initializer.py
from langchain_milvus import Milvus
from langchain_ollama import OllamaEmbeddings

def get_vectorstore():
    embedding_model = OllamaEmbeddings(model="llama3")
    URI = "http://localhost:19530"

    vectorstore = Milvus(
        embedding_function=embedding_model,
        collection_name="rag_data",
        connection_args={"uri": URI, "token": "root:Milvus", "db_name": "milvus_demo"},
        index_params={"index_type": "FLAT", "metric_type": "L2"},
        consistency_level="Strong",
        drop_old=False,
    )
    return vectorstore
