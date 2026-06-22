from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from ollama import chat

DB_DIR = "vector_db"

# Mesmo modelo usado na indexação
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Abre a base vetorial já criada
db = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embeddings
)

pergunta = input("Pergunta: ")

# Busca os 3 documentos mais relevantes
docs = db.similarity_search(
    pergunta,
    k=3
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
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nResposta:\n")
print(resposta["message"]["content"])