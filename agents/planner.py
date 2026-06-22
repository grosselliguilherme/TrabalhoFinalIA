from ollama import chat


class Planner:

    def classify(self, user_input):

        prompt = f"""
Você é um classificador.

Classifique a solicitação abaixo.

Responda SOMENTE com uma palavra:

pergunta
ou
resumo

Solicitação:
{user_input}
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

        result = (
            response["message"]["content"]
            .strip()
            .lower()
        )

        if "resumo" in result:
            return "resumo"

        return "pergunta"