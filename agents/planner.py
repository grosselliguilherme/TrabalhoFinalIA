from ollama import chat
from config import CHAT_MODEL

class Planner:

    def classify(self, user_input):

        texto = user_input.lower()

        palavras_resumo = [
            "resuma",
            "resumo",
            "resumir",
            "faça um resumo",
            "gerar resumo"
        ]

        for palavra in palavras_resumo:
            if palavra in texto:
                return "resumo"

        return "pergunta"