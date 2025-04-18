# RAG for your data

This application is a Retrieval Augmented Generation (RAG) system that allows you to ask questions about your data. You upload your documents, and the application uses a Large Language Model (LLM) to provide answers based on the content of your documents.

## Features

* **Document Upload:** Upload your documents (PDF, DOCX, TXT, CSV, XLSX, JSON).  Limit of 200MB per file.
* **LLM Selection:** Choose from different LLMs (llama3.1, mistral-7b, mixtral-8x7b).
* **Question Answering:** Ask questions about your uploaded documents.
* **Contextual Answers:** The LLM uses the content of your documents to provide relevant answers.
* **Customizable Parameters:**
    * **Top P:** Adjust the Top P sampling parameter.
    * **Top K:** Adjust the Top K retrieval parameter.
    * **Temperature:** Control the randomness of the generated answers.
* **Clear Chat History:** Clear the conversation history.

## How it Works
![RAG Architecture](/Screenshots/rag_arch_dia.png)


## Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/nomanitarique07/RAG_APP.git](https://github.com/nomanitarique07/RAG_APP.git)
    cd RAG_APP
    ```
2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Application:**
    ```bash
    streamlit run app.py
    ```

## Dependencies

The application uses the following main dependencies:

* Streamlit
* LangChain
* (And other libraries listed in `requirements.txt`)

