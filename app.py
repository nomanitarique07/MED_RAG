import streamlit as st
from src.components.sidebar import sidebar
from src.components.uploader import handle_file_upload
from src.module.file_processor import *
from src.module.query_engine import handle_query, query_ollama, query_ollama_2

st.set_page_config(layout="wide")
sidebar()

st.title("RAG for your data")

uploaded_files = st.file_uploader("Upload your documents", type=["pdf", "docx", "txt", "csv", "xlsx", "json"], accept_multiple_files=True)

if uploaded_files:

    if "files_processed" not in st.session_state or not st.session_state["files_processed"]:
        with st.spinner("Processing files and generating embeddings..."):
            handle_file_upload(uploaded_files)
        st.success("Files processed and embedded into vector database.")
        st.session_state["files_processed"] = True
    else:
        st.info("Files already processed and embedded.")

    query = st.text_input("Ask your question:")
    btn = st.button("Ask")
    if btn:
        with st.spinner("Generating answer..."):
            response = handle_query(query)
            print("::Retrieved Chunks::", response)
            print("::END Retrieved Chunks::")
            retrieved_chunks = [ret_chunks['content'] for acc_scr, ret_chunks in response.items()]
            prompt = "\n".join(retrieved_chunks)

            response = query_ollama_2(query, prompt)

            st.markdown(f"{response}")