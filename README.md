DocuMind AI



DocuMind AI is a multi-document RAG (Retrieval-Augmented Generation) assistant that allows users to upload PDF documents, store their embeddings in the Endee vector database, and ask natural language questions over the uploaded coten

Feat
\- Upload one or more PDF documen

\- Extract text from uploaded PDFs
\- Split documents into semantic ch

\- Generate embeddings using Sentence Transformers

\- Store and retrieve vectors using Ende
\- Ask questions in natural langua

\- Generate grounded answers using Gemini

\- Display retrieved source chunks for transparenc


Problem Statement

Finding relevant information from long documents is time-consuming and inefficient. Traditional keyword-based search often misses context and semantic meaning. DocuMind AI solves this by combining vector search and large language models to provide accurate, context-aware answers from uploaded documents.



Solution Overview



DocuMind AI uses a Retrieval-Augmented Generation pipeline:



1\. User uploads PDF documents

2\. Text is extracted and chunked

3\. Each chunk is converted into embeddings

4\. Embeddings are stored in Endee vector database

5\. User asks a question

6\. Relevant chunks are retrieved semantically

7\. Gemini generates an answer based only on retrieved context



Tech Stack



\- Python

\- Streamlit

\- Endee Vector Database

\- Sentence Transformers

\- Gemini API

\- PyMuPDF



Architecture



Upload PDFs → Extract Text → Chunk Text → Generate Embeddings → Store in Endee → Retrieve Relevant Chunks → Generate Answer with Gemini



Project Structure



```bash

documind-ai/

│

├── app.py

├── config.py

├── requirements.txt

├── README.md

├── .env.example

├── docker-compose.yml

├── test\_endee.py

├── test\_gemini\_key.py

│

├── core/

│   ├── extractor.py

│   ├── chunker.py

│   ├── embedder.py

│   ├── vector\_store.py

│   ├── prompts.py

│   └── rag\_pipeline.py

│

└── data/

&#x20;   └── uploads/

