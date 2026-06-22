from agents.orchestrator import Orchestrator


def main():

    orchestrator = Orchestrator()

    print("=" * 40)
    print("\tGuia de Estudos Acadêmicos")
    print("=" * 40)

    while True:

        print("\nDigite sua pergunta.")
        print("Digite 'sair' para encerrar.\n")

        user_input = input("> ")

        if user_input.lower() == "sair":
            print("\nEncerrando...")
            break

        response = orchestrator.process(
            user_input
        )

        print("\nResposta:\n")
        print(response)
        print()


if __name__ == "__main__":
    main()