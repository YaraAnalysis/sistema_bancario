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

    elif opcao == 2:
        print(f"Opção escolhida: {opcao} - Saque.")

        if numero_saques >= 3:
            print("Não é  possível realizar o saque. Você excedeu o limite diário de 3 saques.")
        else:
            print(f"Saldo: R$ {saldo:.2f}")
            valor_saque = float(input("Qual o valor do saque? "))

            if valor_saque > saldo:
                print("Operação falhou. Você não tem saldo suficiente.")
            
            elif valor_saque > 500:
                print("Operação falhou. O valor solicitado excede o limite.")

            elif valor_saque <= 500 and saldo >= valor_saque:
                print(f"Saque efetuado no valor de R$ {valor_saque:.2f}")
                extrato += f"Saque de R$ {valor_saque:.2f}\n"
                saldo = saldo - valor_saque
                numero_saques += 1

    elif opcao == 3:
        print(f"Opção escolhida: {opcao} - Extrato.")
        print("Extrato".center(31, "="))
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {valor:.2f}")
        print("Fim do Extrato".center(31, "="))

    elif opcao == 0:
        print(f"Opção escolhida: {opcao} - Sair.")
        break

    else:
        print("Opção inválida. Selecione novamente a opção desejada.")

