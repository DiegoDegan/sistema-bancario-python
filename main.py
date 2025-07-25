menu = """
##########  BEM-VINDO  ##########

    Selecione a opção desejada:

[S] SAQUE
[D] DEPOSITO
[E] EXTRATO

[q] SAIR
"""

saldo = 0
extrato = ""
limite = 500
saques_realizados = 0
LIMITE_SAQUES = 3

def voltar_menu():
    while True:
        voltar = input("Insira 'M' para voltar ao menu principal: ").strip().lower()
        if voltar == "m":
            break
        else:
            print("Entrada inválida. Digite apenas M.")

while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
            continue

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Valor R$ {valor:.2f} depositado com sucesso.")
            voltar_menu()

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
            continue

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = saques_realizados >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saques_realizados += 1
            print("Saque realizado com sucesso.")
            voltar_menu()

        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        voltar_menu()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")