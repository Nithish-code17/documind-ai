from config import GEMINI_API_KEY

print("Key found:", bool(GEMINI_API_KEY))
print("First 10 chars:", GEMINI_API_KEY[:10] if GEMINI_API_KEY else "EMPTY")