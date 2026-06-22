import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from agents.orchestrator import Orchestrator

orchestrator = Orchestrator()

response = orchestrator.process(
    "O que é TCP?"
)

print("\nResposta:\n")

print(response)