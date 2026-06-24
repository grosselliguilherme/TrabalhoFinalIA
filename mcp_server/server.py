from pathlib import Path
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from fastmcp import FastMCP
from config import (
    EMBED_MODEL,
    DB_DIR,
    TOP_K
)

mcp = FastMCP("Guia de Estudos Acadêmicos")

embeddings = OllamaEmbeddings(
    model=EMBED_MODEL
)

db = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embeddings
)

@mcp.tool()
def listar_disciplinas():
    return [
        "Redes",
        "Inteligência Artificial",
        "Algoritmos"
    ]

@mcp.tool()
def buscar_conteudo(pergunta: str):
    docs = db.similarity_search(
        pergunta,
        k=TOP_K
    )

    return [
        doc.page_content
        for doc in docs
    ]

if __name__ == "__main__":
    mcp.run()