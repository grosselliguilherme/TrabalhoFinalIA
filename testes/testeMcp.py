import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from mcp_server.server import listar_disciplinas

print(
    listar_disciplinas()
)