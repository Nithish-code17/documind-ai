from sentence_transformers import SentenceTransformer
from config import EMBED_MODEL

_model = SentenceTransformer(EMBED_MODEL)

def embed_texts(texts):
    return _model.encode(texts, convert_to_numpy=True).tolist()

def embed_query(query: str):
    return _model.encode([query], convert_to_numpy=True)[0].tolist()