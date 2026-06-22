import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from mcp_server.server import buscar_conteudo

resultado = buscar_conteudo(
    "O que é TCP?"
)

for item in resultado:
    print("\n---\n")
    print(item)