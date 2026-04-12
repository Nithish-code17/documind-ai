from endee import Endee, Precision
from endee.exceptions import ConflictException
from config import ENDEE_BASE_URL, INDEX_NAME, EMBED_DIMENSION

def get_client():
    client = Endee()
    client.set_base_url(ENDEE_BASE_URL)
    return client

def ensure_index():
    client = get_client()

    try:
        client.create_index(
            name=INDEX_NAME,
            dimension=EMBED_DIMENSION,
            space_type="cosine",
            precision=Precision.INT8
        )
        print(f"Created index: {INDEX_NAME}")
    except ConflictException:
        print(f"Index already exists: {INDEX_NAME}")

    return client.get_index(INDEX_NAME)

def upsert_chunks(chunks, vectors, source_name):
    index = ensure_index()

    payload = []
    for i, (chunk, vector) in enumerate(zip(chunks, vectors)):
        payload.append({
            "id": f"{source_name}_{i}",
            "vector": vector,
            "meta": {
                "source": source_name,
                "chunk_id": i,
                "text": chunk
            },
            "filter": {
                "source": source_name
            }
        })

    index.upsert(payload)

def search_chunks(query_vector, top_k=5):
    index = ensure_index()
    return index.query(
        vector=query_vector,
        top_k=top_k
    )