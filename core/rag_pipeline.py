from google import genai
from config import TOP_K, GEMINI_API_KEY
from core.embedder import embed_query
from core.vector_store import search_chunks
from core.prompts import RAG_PROMPT

client = genai.Client(api_key=GEMINI_API_KEY)

def retrieve_context(question: str, top_k: int = TOP_K):
    q_vector = embed_query(question)
    results = search_chunks(q_vector, top_k=top_k)

    contexts = []
    for item in results:
        meta = item.get("meta", {})
        contexts.append({
            "source": meta.get("source", "unknown"),
            "text": meta.get("text", ""),
            "similarity": item.get("similarity", None)
        })

    return contexts

def answer_question(question: str):
    contexts = retrieve_context(question)

    context_text = "\n\n".join(
        [f"[Source: {c['source']}]\n{c['text']}" for c in contexts]
    )

    prompt = RAG_PROMPT.format(
        context=context_text,
        question=question
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    answer_text = getattr(response, "text", None)
    if not answer_text:
        answer_text = "I could not generate an answer."

    return answer_text, contexts