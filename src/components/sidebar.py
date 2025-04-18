import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import *

def sidebar():
    st.sidebar.title("Select LLM Model")

    LLM_CONFIG["model"] = st.sidebar.radio(
        "Model",
        options=[
            "llama3.1",
        ],
        index=0
    )

    #LLM_CONFIG["max_tokens"] = st.sidebar.slider("Max Tokens", min_value=10, max_value=500, value=LLM_CONFIG["max_tokens"])
    LLM_CONFIG["top_p"] = st.sidebar.slider("Top P", min_value=0.0, max_value=1.0, value=LLM_CONFIG["top_p"], step=0.01)
    LLM_CONFIG["top_k"] = st.sidebar.slider("Top K", min_value=0, max_value=100, value=LLM_CONFIG["top_k"])
    LLM_CONFIG["temperature"] = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=LLM_CONFIG["temperature"], step=0.01)

    #LLM_CONFIG["token_key"] = st.sidebar.text_input("Token Key", value=LLM_CONFIG["token_key"], type="password")

    if st.sidebar.button("Clear Chat History"):
        st.session_state.clear()