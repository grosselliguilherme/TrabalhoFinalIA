import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from agents.executor import Executor

executor = Executor()

context = """
TCP utiliza three-way handshake.

1. SYN
2. SYN-ACK
3. ACK
"""

answer = executor.answer(
    "Como funciona o handshake?",
    context
)

print(answer)