
contas = [
    {"nome": "João", "saldo": 1500, "historico": []},
    {"nome": "Maria", "saldo": 2300, "historico": []},
    {"nome": "Carlos", "saldo": 500, "historico": []},
]

def buscar_conta(nome):
    for conta in contas:
        if conta["nome"].lower() == nome.lower():
            return conta
    return None

def depositar(conta, valor):
    if valor <= 0:
        print("Valor inválido.")
        return
    conta["saldo"] += valor
    conta["historico"].append(f"Depósito: +{valor}")
    print("Depósito realizado.")

def sacar(conta, valor):
    if valor <= 0:
        print("Valor inválido.")
        return
    if conta["saldo"] >= valor:
        conta["saldo"] -= valor
        conta["historico"].append(f"Saque: -{valor}")
        print("Saque realizado.")
    else:
        print("Saldo insuficiente.")

def transferir(origem, destino, valor):
    if valor <= 0:
        print("Valor inválido.")
        return
    if origem["saldo"] >= valor:
        origem["saldo"] -= valor
        destino["saldo"] += valor
        origem["historico"].append(f"Transferência enviada para {destino['nome']}: -{valor}")
        destino["historico"].append(f"Transferência recebida de {origem['nome']}: +{valor}")
        print("Transferência realizada.")
    else:
        print("Saldo insuficiente.")

def mostrar_historico(conta):
    print(f"\nHistórico de {conta['nome']}:")
    if not conta["historico"]:
        print("Nenhuma operação realizada.")
    else:
        for item in conta["historico"]:
            print(item)

def menu():
    while True:
        print("\n=== BANCO ===")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Transferir")
        print("4 - Histórico")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome da conta: ")
            conta = buscar_conta(nome)
            if conta:
                valor = float(input("Valor: "))
                depositar(conta, valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "2":
            nome = input("Nome da conta: ")
            conta = buscar_conta(nome)
            if conta:
                valor = float(input("Valor: "))
                sacar(conta, valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "3":
            nome1 = input("Conta origem: ")
            nome2 = input("Conta destino: ")
            origem = buscar_conta(nome1)
            destino = buscar_conta(nome2)

            if origem and destino:
                valor = float(input("Valor: "))
                transferir(origem, destino, valor)
            else:
                print("Conta inválida.")

        elif opcao == "4":
            nome = input("Nome da conta: ")
            conta = buscar_conta(nome)
            if conta:
                mostrar_historico(conta)
            else:
                print("Conta não encontrada.")

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

menu()
