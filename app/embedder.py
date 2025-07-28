from sentence_transformers import SentenceTransformer

def get_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(model, texts):
    return model.encode(texts, convert_to_tensor=True)
