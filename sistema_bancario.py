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
            extrato += f"Depósito de R$ {valor:.2f}"
            # print(extrato)
            # print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == 2:
        print(f"Opção escolhida: {opcao} - Saque.")
        # desenvolver lógica de saque

    elif opcao == 3:
        print(f"Opção escolhida: {opcao} - Extrato.")
        # desenvolver lógica de extrato

    elif opcao == 0:
        print(f"Opção escolhida: {opcao} - Sair.")
        break
        # sair

    else:
        print("Opção inválida. Selecione novamente a opção desejada.")

