titular = input("Digite o nome do titular da conta: ")
saldo = 0

while True:
    print("\nMenu Principal:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Verificar Saldo")
    print("4. Sair")

    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        valor = float(input("Digite o valor para depósito: "))
        if valor > 0:
            saldo += valor
            print(f'Depósito de R${valor} realizado com sucesso. Novo saldo: R${saldo}')
        else:
            print('Valor de depósito inválido.')
    elif opcao == "2":
        valor = float(input("Digite o valor para saque: "))
        if valor > 0 and valor <= saldo:
            saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso. Novo saldo: R${saldo}')
        else:
            print('Saldo insuficiente ou valor de saque inválido.')
    elif opcao == "3":
        print(f'Saldo atual da conta de {titular}: R${saldo}')
    elif opcao == "4":
        print("Saindo do programa. Obrigado!")
        break
    else:
        print("Opção inválida. Tente novamente.")