import random

participantes = []

print("=== SISTEMA DE SORTEIO ===")

while True:
    print("\n1 - Adicionar participante(s)")
    print("2 - Realizar sorteio")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        entrada = input("Digite o(s) nome(s) do(s) participante(s) (separados por vírgula): ").strip()

        if entrada == "":
            print("⚠️ Nome vazio não é permitido.")
        else:
            nomes = [n.strip() for n in entrada.split(",") if n.strip()]

            for nome in nomes:
                if nome in participantes:
                    print(f"⚠️ {nome} já foi adicionado.")
                else:
                    participantes.append(nome)
                    print(f"✅ {nome} adicionado com sucesso!")

    elif opcao == "2":
        if len(participantes) < 2:
            print("⚠️ É necessário pelo menos 2 participantes para sortear.")
        else:
            sorteado = random.choice(participantes)
            print(f"\n🎉 O sorteado foi: {sorteado}")

    elif opcao == "3":
        print("Encerrando o sistema...")
        break

    else:
        print("⚠️ Opção inválida.")




