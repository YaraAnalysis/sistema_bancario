def menu():
    menu = '''

    *********************************
    Bem vindo à sua conta bancária.
    Ecolha uma opção:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
    '''
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
        print(45 * "=")
        print(f"Depósito efetuado com sucesso! Valor: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(45 * "=")
    else:
        print(" Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def main():
    LIMITE_SAQUES = 3
    
    saldo = 0
    extrato = ""
    valor_maximo_saque = 500
    numero_saques = 0

    while True:
        opcao = int(menu())

        if opcao == 1:
            print(f"Opção escolhida: {opcao} - Depósito.")
            valor = float(input("Qual o valor do depósito? "))

            saldo, extrato = depositar(saldo, valor, extrato)
            

        elif opcao == 2:
            print(f"Opção escolhida: {opcao} - Saque.")

            if numero_saques >= 3:
                print("Não é  possível realizar o saque. Você excedeu o limite diário de 3 saques.")
            else:
                valor_saque = float(input("Qual o valor do saque? "))

                if valor_saque > saldo:
                    print(55 * "=")
                    print("Operação falhou. Você não tem saldo suficiente.")
                    print(55 * "=")
                
                elif valor_saque > 500:
                    print(55 * "=")
                    print("Operação falhou. O valor solicitado excede o limite.")
                    print(55 * "=")

                elif valor_saque <= 500 and saldo >= valor_saque:
                    print(55 * "=")
                    print(f"Saque efetuado no valor de R$ {valor_saque:.2f}")
                    print(55 * "=")
                    extrato += f"Saque de R$ {valor_saque:.2f}\n"
                    saldo = saldo - valor_saque
                    numero_saques += 1

        elif opcao == 3:
            print(f"Opção escolhida: {opcao} - Extrato.")
            print("Extrato".center(45, "="))
            print(extrato if extrato else "Não foram realizadas movimentações.")
            print(f"Saldo atual: R$ {saldo:.2f}")
            print("Fim do Extrato".center(45, "="))

        elif opcao == 0:
            print(f"Opção escolhida: {opcao} - Sair.")
            break

        else:
            print("Opção inválida. Selecione novamente a opção desejada.")


main()