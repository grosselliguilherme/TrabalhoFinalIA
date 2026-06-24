from ollama import chat
from config import CHAT_MODEL

class Executor:
    def answer(
        self,
        question,
        context
    ):

        prompt = f"""
        Você é um assistente acadêmico especializado em conteúdos universitários.

        Regras:
        - Utilize apenas o contexto fornecido.
        - Não invente informações.
        - Se a resposta não estiver no contexto, responda:
        "Não encontrei essa informação na base de estudos."
        - Seja claro e didático.
        - Responda em português.

        Contexto:
        {context}

        Pergunta:
        {question}

        Resposta:
        """

        response = chat(
            model=CHAT_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    def summarize(
        self,
        context
    ):

        prompt = f"""
        Você é um assistente acadêmico.

        Faça um resumo acadêmico do conteúdo.

        Regras:
        - Utilize apenas o conteúdo fornecido.
        - Não invente informações.
        - Organize a resposta em tópicos.
        - Destaque apenas os conceitos principais.
        - Ignore exemplos irrelevantes e informações secundárias.
        - Responda em português.

        Conteúdo:
        {context}

        Resumo:
        """

        response = chat(
            model=CHAT_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]