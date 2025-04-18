import requests
from sentence_transformers import SentenceTransformer
from langchain_chroma import Chroma
from pymilvus import Collection, MilvusException, connections, db, utility
from langchain_milvus import BM25BuiltInFunction, Milvus
from config import EMBEDDING_MODEL, LLM_CONFIG, VECTORDB_CONFIG, DB_DIR
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
# from src.module.embedder_chroma import CustomSentenceTransformerEmbedding
from langchain_ollama import OllamaEmbeddings
import ollama
from src.module.embedder import get_vectorstore

vectorstore = get_vectorstore()  # Reuse existing store

#embedding_model = SentenceTransformer(EMBEDDING_MODEL)
#embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
#embedding_model = CustomSentenceTransformerEmbedding()
embedding_model = OllamaEmbeddings(
        model="llama3",
    )

def handle_query(query):

    results = vectorstore.similarity_search_with_score(
        query, k=10
    )

    result = {}
    for i, (res, score) in enumerate(results):
        result[i] = {
            "score": score,
            "content": res.page_content
        }

    return result

def query_ollama_2(query, context):
    client = ollama.Client()
    model = "llama3.1"
    prompt = f"""You are a smart helpful assistant that answers concisely to a user query.
        
        user query: {query}
        retrieved context: {context}
        \n Use below chain of thought for response generation.

        STEP 1: Based on the user query received. Respond to the user as a health care insurer expert in most professional way.
        STEP 2: Once you have the response, try to give accurate, precise information from retrieved context only. DO NOT generate response outside the context OR assume any information that is not present in the context.
        STEP 3: Results are mostly about cost share details like copay, coinsurance, deductible, plan, out of pocket, in network, out of netowrk etc. Articulate the response based on the user question and context.
        
        IMPORTANT NOTE: 
        1) DO NOT assume or guess the data. Give the accurate, concise and to the point response to a query. DO NOT generate any extra text which is out of context. If the user question is out of context (i.e. not from health care insurance or medical Plan related information) then simply return |I don't know|.
        2) Only give response and do not explain the response.
        3) DO NOT add salutation in the beggening or end.
        
        """
    response = client.generate(model=model, 
                               prompt=prompt,
                               options={
                        "temperature": LLM_CONFIG["temperature"],
                        "top_p": LLM_CONFIG["top_p"],
                        "top_k": LLM_CONFIG["top_k"],
                        "num_predict": LLM_CONFIG["max_tokens"]
                    }
                )
    print(":::RAW Response:::", response.response)
    print(":::RAW END:::")
    return response.response

        
def query_ollama(prompt):
    payload = {
        "model": LLM_CONFIG["model"],
        "prompt": prompt,
        # "stream": True,
        "options": {
            "temperature": LLM_CONFIG["temperature"],
            "top_p": LLM_CONFIG["top_p"],
            "top_k": LLM_CONFIG["top_k"],
            "num_predict": LLM_CONFIG["max_tokens"]
        }
    }

    headers = {
        "Authorization": f"Bearer {LLM_CONFIG['token_key']}",
        "Content-Type": "application/json"
    }

    response = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)
    return response.json().get("response", "No response")

