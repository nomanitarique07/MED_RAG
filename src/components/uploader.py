import os
import streamlit as st
from src.module.file_processor import *
from src.module.embedder import embed_and_store
#from src.module.embedder_chroma import embed_and_store
from config import TEMP_DIR

def handle_file_upload(uploaded_files):

    for file in uploaded_files:
        file_path = os.path.join(TEMP_DIR, file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())

        content = extract_text_from_file(file_path)
        text_chunks = split_document(content)
        
    if "vectorstore_initialized" not in st.session_state:
        vectorstore = embed_and_store(text_chunks)
        st.session_state["vectorstore_initialized"] = True
    #embed_and_store(text_chunks)

    return content