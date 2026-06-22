# test_ollama.py

import requests
import sys

print(sys.executable)

url = "http://localhost:11434/api/generate"

response = requests.post(
    url,
    json={
        "model": "llama3.2",
        "prompt": "Explique o que é TCP.",
        "stream": False
    }
)

print(response.json()["response"])