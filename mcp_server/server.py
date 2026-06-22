from pathlib import Path
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from fastmcp import FastMCP

mcp = FastMCP("Guia de Estudos Acadêmicos")


@mcp.tool()
def listar_disciplinas():
    return [
        "Redes",
        "Inteligência Artificial",
        "Algoritmos"
    ]


@mcp.tool()
def buscar_conteudo(pergunta: str):

    db = Chroma(
        persist_directory="vector_db",
        embedding_function=OllamaEmbeddings(
            model="nomic-embed-text"
        )
    )

    docs = db.similarity_search(
        pergunta,
        k=3
    )

    return [
        doc.page_content
        for doc in docs
    ]


if __name__ == "__main__":
    mcp.run()