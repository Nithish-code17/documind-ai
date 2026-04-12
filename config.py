import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")
ENDEE_BASE_URL = os.getenv("ENDEE_BASE_URL", "http://localhost:8080/api/v1")
INDEX_NAME = os.getenv("INDEX_NAME", "documind_index")

CHUNK_SIZE = 700
CHUNK_OVERLAP = 120
TOP_K = 5
EMBED_DIMENSION = 384