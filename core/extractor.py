import fitz
from pathlib import Path

def extract_text_from_pdf(pdf_path: str) -> str:
    text_parts = []
    doc = fitz.open(pdf_path)
    for page in doc:
        text_parts.append(page.get_text("text"))
    doc.close()
    return "\n".join(text_parts)

def save_uploaded_file(uploaded_file, save_dir="data/uploads") -> str:
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    file_path = Path(save_dir) / uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return str(file_path)