# from sentence_transformers import SentenceTransformer
# from langchain_chroma import Chroma
# from uuid import uuid4
# from langchain_core.documents import Document
# from langchain_huggingface.embeddings import HuggingFaceEmbeddings
# from langchain_core.embeddings import Embeddings

# from config import EMBEDDING_MODEL,VECTORDB_CONFIG,DB_DIR

# #model = SentenceTransformer(EMBEDDING_MODEL)
# #model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# # Custom embedding wrapper
# class CustomSentenceTransformerEmbedding(Embeddings):
#     def __init__(self, model_name="sentence-transformers/all-mpnet-base-v2"):
#         self.model = SentenceTransformer(model_name)

#     def embed_documents(self, texts):
#         return self.model.encode(texts, show_progress_bar=False)

#     def embed_query(self, text):
#         return self.model.encode([text])[0]    

# def embed_and_store(text_chunks):

#     documents = []
#     # text_chunks is a list
#     for text_chunk in text_chunks:
#         documents.append(Document(str(text_chunk.page_content)))
        
#     uuids = [str(uuid4()) for _ in range(len(documents))]

#      # Step 3: Initialize custom embedding wrapper
#     embedding_model = CustomSentenceTransformerEmbedding()

#     # Step 4: Create vector store instance
#     vector_store = Chroma(
#         collection_name = "rag_data",
#         embedding_function=embedding_model,
#         persist_directory=DB_DIR  # make sure this is defined in config
#     )

#     vector_store.add_documents(documents=documents, ids=uuids)

#     # embeddings = model.encode(text_chunks, normalize_embeddings=True).tolist()
    
#     # data = [embeddings, text_chunks]
    