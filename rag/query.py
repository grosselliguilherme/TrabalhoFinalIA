# arquivo para testes de RAG
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from ollama import chat
from pathlib import Path
import sys

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from config import (
    CHAT_MODEL,
    EMBED_MODEL,
    DB_DIR,
    TOP_K
)

# modelo usado na indexação
embeddings = OllamaEmbeddings(model=EMBED_MODEL)

# Abre a base vetorial já criada
db = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embeddings
)

pergunta = input("Pergunta: ")

# Busca os 3 documentos mais relevantes
docs = db.similarity_search(
    pergunta,
    k=TOP_K
)

contexto = "\n\n".join(
    doc.page_content
    for doc in docs
)

prompt = f"""
Você é um assistente acadêmico.

Utilize APENAS o contexto fornecido.

Contexto:
{contexto}

Pergunta:
{pergunta}

Resposta:
"""

resposta = chat(
    model=CHAT_MODEL,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nResposta:\n")
print(resposta["message"]["content"])