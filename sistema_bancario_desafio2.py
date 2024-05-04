def menu():
    menu = '''

    *********************************
    Bem vindo à sua conta bancária.
    Ecolha uma opção:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar contas
    [0] Sair
    '''
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
        print(45 * "=")
        print(f"=== Depósito efetuado com sucesso! Valor: R$ {valor:.2f} ===")
        print(f"=== Saldo atual: R$ {saldo:.2f} ===")
        print(45 * "=")
    else:
        print("XXX Operação falhou! O valor informado é inválido. XXX")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, valor_maximo_saque, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > valor_maximo_saque
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("XXX Operação falhou! Você não tem saldo suficiente. XXX")
   
    elif excedeu_limite:
        print("XXX Operação falhou! O valor solicitado excede o limite. XXX")
    
    elif excedeu_saques:
        print("XXX Operação falhou! Você excedeu o limite diário de 3 saques. XXX")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"=== Saque efetuado com sucesso! Valor: R$ {valor:.2f} ===")
        # print(f"Número de saques efetuados: {numero_saques}.")
    else:
        print("XXX Operação falhou! O valor informado é inválido. XXX")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("Extrato".center(45, "="))
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("Fim do Extrato".center(45, "="))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nXXX Já existe usuário com esse CPF! XXX")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
           Agência:\t{conta['agencia']}
           C/C:\t\t{conta['numero_conta']}
           Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = 1

    saldo = 0
    extrato = ""
    valor_maximo_saque = 500
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = int(menu())

        if opcao == 1:
            print(f"Opção escolhida: {opcao} - Depósito.")
            valor = float(input("Qual o valor do depósito? "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            print(f"Opção escolhida: {opcao} - Saque.")
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo, 
                valor=valor,
                extrato=extrato,
                valor_maximo_saque=valor_maximo_saque,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
         criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 6:
            listar_contas(contas)
            
        elif opcao == 0:
            print(f"Opção escolhida: {opcao} - Sair.")
            break

        else:
            print("Opção inválida. Selecione novamente a opção desejada.")


main()