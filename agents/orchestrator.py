from agents.planner import Planner
from agents.researcher import Researcher
from agents.executor import Executor


class Orchestrator:

    def __init__(self):

        self.planner = Planner()

        self.researcher = Researcher()

        self.executor = Executor()

    def process(self, user_input):

        task = self.planner.classify(
            user_input
        )

        print(
            f"[Planner] Tipo identificado: {task}"
        )

        if task == "pergunta":

            query = (
                user_input
                .replace("Resuma", "")
                .replace("resuma", "")
                .strip()
            )

            docs = self.researcher.search(
                query
            )

            context = "\n\n".join(docs)

            return self.executor.answer(
                user_input,
                context
            )

        if task == "resumo":

            docs = self.researcher.search(
                user_input
            )

            context = "\n\n".join(
                doc.page_content
                for doc in docs
            )

            return self.executor.summarize(
                context
            )
        
        return (
            f"Tipo '{task}' ainda não implementado."
        )
        