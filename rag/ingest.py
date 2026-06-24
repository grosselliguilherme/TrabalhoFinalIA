from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from config import (
    EMBED_MODEL,
    DB_DIR
)

BASE_DIR = Path("base_dados")

documents = []

for file in BASE_DIR.rglob("*.md"):
    content = file.read_text(encoding="utf-8")

    documents.append(
        Document(
            page_content=content,
            metadata={
                "source": str(file)
            }
        )
    )


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

embeddings = OllamaEmbeddings(model=EMBED_MODEL)

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_DIR
)

print(f"{len(chunks)} chunks indexados.")