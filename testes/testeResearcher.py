import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from agents.researcher import Researcher

researcher = Researcher()

docs = researcher.search("O que é TCP?")

for doc in docs:
    print("\n---\n")
    print(doc)