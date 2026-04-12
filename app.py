import streamlit as st
from core.extractor import extract_text_from_pdf, save_uploaded_file
from core.chunker import chunk_text
from core.embedder import embed_texts
from core.vector_store import upsert_chunks, ensure_index
from core.rag_pipeline import answer_question

st.set_page_config(page_title="DocuMind AI", layout="wide")
st.title("DocuMind AI")
st.subheader("Multi-Document RAG Assistant using Endee Vector Database")

ensure_index()

if "processed_files" not in st.session_state:
    st.session_state.processed_files = []

if "total_chunks" not in st.session_state:
    st.session_state.total_chunks = 0

st.markdown("### Upload PDF Documents")
uploaded_files = st.file_uploader(
    "Upload one or more PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Process Documents"):
        if not uploaded_files:
            st.warning("Please upload at least one PDF.")
        else:
            with st.spinner("Extracting, chunking, embedding, and storing documents..."):
                total_chunks = 0
                processed_names = []

                for uploaded_file in uploaded_files:
                    file_path = save_uploaded_file(uploaded_file)
                    raw_text = extract_text_from_pdf(file_path)

                    if not raw_text.strip():
                        st.error(f"No readable text found in {uploaded_file.name}")
                        continue

                    chunks = chunk_text(raw_text)
                    vectors = embed_texts(chunks)
                    upsert_chunks(chunks, vectors, uploaded_file.name)

                    total_chunks += len(chunks)
                    processed_names.append(uploaded_file.name)

                st.session_state.processed_files = processed_names
                st.session_state.total_chunks = total_chunks

            st.success(f"Processed {len(processed_names)} file(s) and stored {total_chunks} chunks.")

with col2:
    if st.button("Clear Session Info"):
        st.session_state.processed_files = []
        st.session_state.total_chunks = 0
        st.rerun()

if st.session_state.processed_files:
    st.markdown("### Processed Files")
    for file_name in st.session_state.processed_files:
        st.write(f"- {file_name}")
    st.caption(f"Total chunks stored in current session: {st.session_state.total_chunks}")

st.markdown("---")
st.markdown("### Ask Questions")
question = st.text_input("Enter your question")

if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Retrieving relevant chunks and generating answer..."):
            answer, contexts = answer_question(question)

        st.markdown("## Answer")
        st.write(answer)

        st.markdown("## Retrieved Sources")
        for i, c in enumerate(contexts, 1):
            with st.expander(f"Source {i} - {c['source']}"):
                st.write(c["text"])
                if c["similarity"] is not None:
                    st.caption(f"Similarity: {c['similarity']:.4f}")