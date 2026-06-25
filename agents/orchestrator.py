from agents.planner import Planner
from agents.researcher import Researcher
from agents.executor import Executor

class Orchestrator:

    def __init__(self):
        self.planner = Planner()
        self.researcher = Researcher()
        self.executor = Executor()

    def process(self, user_input):

        task = self.planner.classify(user_input)

        query = (
            user_input
            .replace("Resuma", "")
            .replace("resuma", "")
            .strip()
        )

        docs = self.researcher.search(query)

        if not docs:
            return (
                "Não encontrei essa informação "
                "na base de estudos."
            )

        context = "\n\n".join(docs)

        if task == "resumo":
            return self.executor.summarize(context)

        return self.executor.answer(
            user_input,
            context
        )