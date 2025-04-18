import os
import pandas as pd
import PyPDF2
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.utils.docling_processor import call_docling


def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf_using_docling(file_path)
        #return extract_text_from_pdf(file_path)
    elif ext == ".txt":
        return extract_text_from_txt(file_path)
    elif ext in [".csv", ".xlsx"]:
        return extract_text_from_spreadsheet(file_path)
    elif ext == ".json":
        return extract_text_from_json(file_path)
    else:
        return ""

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_pdf_using_docling(file_path):
    text = call_docling(file_path)
    print(":::TEXT VIA DOCLING:::", text)
    return text

def split_document(content):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    texts = text_splitter.create_documents([content])
    
    return texts

def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def extract_text_from_spreadsheet(file_path):
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
        return df.to_string(index=False)
    except Exception as e:
        return f"Error reading spreadsheet: {e}"

def extract_text_from_json(file_path):
    import json
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return str(data)
    except Exception as e:
        return f"Error reading JSON: {e}"
