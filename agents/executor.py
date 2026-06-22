from ollama import chat


class Executor:

    def answer(
        self,
        question,
        context
    ):

        prompt = f"""
Você é um assistente acadêmico.

Utilize APENAS o contexto fornecido.

Contexto:
{context}

Pergunta:
{question}

Resposta:
"""

        response = chat(
            model="llama3.2",
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

Faça um resumo claro e objetivo
do conteúdo abaixo.

Conteúdo:
{context}
"""

        response = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]