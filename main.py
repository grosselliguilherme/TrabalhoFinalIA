from agents.orchestrator import Orchestrator

def main():

    orchestrator = Orchestrator()

    print("\n" + "=" * 45)
    print("      GAE - Guia de Estudos Acadêmicos")
    print("\n     Assistente Inteligente para Estudos\n")
    print("=" * 45)

    print("Exemplos de comandos:")
    print("- \"O que é TCP?\" ou \"Resuma TCP\".")

    print("\nDigite 'sair' para encerrar o assistente.\n")

    while True:
        user_input = input("\nO que você deseja? > ")

        if user_input.lower() == "sair":
            print("\nEncerrando...")
            break

        response = orchestrator.process(user_input)

        print("\n" + "-" * 30)
        print("Resposta")
        print("-" * 30 + "\n")
        print(response)
        print()


if __name__ == "__main__":
    main()