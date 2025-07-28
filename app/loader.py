import json
import os
import fitz

def load_input(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_pdfs(pdf_folder):
    documents = []
    for fname in sorted(os.listdir(pdf_folder)):
        if fname.endswith(".pdf"):
            path = os.path.join(pdf_folder, fname)
            doc = fitz.open(path)
            documents.append((fname, doc))
    return documents
