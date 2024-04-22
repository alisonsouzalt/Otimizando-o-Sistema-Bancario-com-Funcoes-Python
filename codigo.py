def menu_2():
    menu_dois = """

    [1] Criar Usuário
    [2] Criar Conta
    [3] Depósito
    [4] Saque
    [5] Extrato
    [6] Consultar contas
    [0] Sair 
    ==> """
    return input(menu_dois)

def cadastro_usuario(usuarios):
    cpf = input("Digite seu CPF: ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("\nEste CPF já está cadastrado!")
        return
    else:
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite sua data nascimento (dd-mm-aa): ")
        endereco = input("Digite seu enderço (logradouro - nº - bairro - cidade/sigla estado): ")
        
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print("\nUsuário cadastrado com sucesso!")


def buscar_usuario(cpf, usuarios):
    checar_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return checar_usuario [0] if checar_usuario else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF: ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("\nUsuário não cadastrado!")

def deposito(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
        return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUE):

    if valor > saldo:
        print("\nVocê não tem saldo suficiente.")

    elif valor > limite:
        print("\nO valor do saque excede o limite.")

    elif numero_saques >= LIMITE_SAQUE:
        print("\nNúmero máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")

    else:
        print("\nO valor informado é inválido.")

    return saldo, extrato

def consultar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def listar_contas(contas):
    print(f"""Lista de contas\n {contas[::]}""")
    return

def main():
    usuarios = []
    contas = []
    saldo = 0
    extrato = ""
    AGENCIA = "0001"
    LIMITE_SAQUE = 3
    limite = 500
    numero_saques = 0
    while True:
        opcao = menu_2()
        if opcao == "1":
            cadastro_usuario(usuarios)
        
        elif opcao == "2":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "3":
            valor = int(input("Digite o valor de depósito: "))
            saldo, extrato = deposito(valor, saldo, extrato)

        elif opcao == "4":
            valor = float(input("Digite o valor de saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUE=LIMITE_SAQUE,
            )

        elif opcao == "5":
            consultar_extrato(saldo, extrato=extrato)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("Sistema Finalizado!")
            break


main()
