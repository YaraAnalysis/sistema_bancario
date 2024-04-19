menu = '''
Bem vindo à sua conta bancária.
Ecolha uma opção:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
Escolha a sua opção: 
'''

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print(f"Opção escolhida: {opcao}.")
        # desenvolver lógica de depósito
    elif opcao == 2:
        print(f"Opção escolhida: {opcao}.")
        # desenvolver lógica de saque
    elif opcao == 3:
        print(f"Opção escolhida: {opcao}.")
        # desenvolver lógica de extrato
    elif opcao == 0:
        print(f"Opção escolhida: {opcao}.")
        break
        # sair
    else:
        print("Opção inválida. Selecione novamente a opção desejada.")

