import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from agents.planner import Planner

planner = Planner()

print(
    planner.classify(
        "O que é TCP?"
    )
)

print(
    planner.classify(
        "Resuma TCP"
    )
)