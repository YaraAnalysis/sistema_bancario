menu = '''
===============================
Bem vindo à sua conta bancária.
Ecolha uma opção:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
Escolha a sua opção: 
'''

saldo = 0
extrato = ""
valor_maximo_saque = 500
limite_saques = 3
numero_saques = 0

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print(f"Opção escolhida: {opcao} - Depósito.")

        valor = float(input("Qual o valor do depósito? "))

        if valor > 0:
            saldo += valor
            print(f"Valor depositado: R$ {valor:.2f}")
            extrato += f"Depósito de R$ {valor:.2f}\n"
            # print(extrato)
            # print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == 2:
        print(f"Opção escolhida: {opcao} - Saque.")
        # desenvolver lógica de saque

        if numero_saques >= 3:
            print("Não foi possível realizar o saque. Você excedeu o limite diário de 3 saques.")
        else:
            valor = float(input("Qual o valor do saque? "))

            if valor <= 500 and saldo >= valor:
                print(f"Saque efetuado no valor de R$ {valor:.2f}")
                extrato += f"Saque de R$ {valor:.2f}\n"
                saldo -= valor
                numero_saques += 1
                # print(extrato)
                # print(f"Saldo: R$ {saldo:.2f}")
            elif valor > 500:
                print("Operação falhou. O valor solicitado excede o limite.")
            elif valor > saldo:
                print("Operação falhou. Você não tem saldo suficiente.")


    elif opcao == 3:
        print(f"Opção escolhida: {opcao} - Extrato.")
        # desenvolver lógica de extrato
        print("Extrato".center(31, "="))
        print(extrato if extrato else "Não foram realizadas movimentações.")

    elif opcao == 0:
        print(f"Opção escolhida: {opcao} - Sair.")
        break
        # sair

    else:
        print("Opção inválida. Selecione novamente a opção desejada.")

