menu = """
   BANCO MEGASMART
______________________
|                    |
|[1] Depositar       |
|[2] Sacar           |
|[3] Extrato         |
|[0] Sair            |
|____________________|

| Digite sua opção:
| => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("\nInforme o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Falha na operação! Valor inválido.")

    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('\nFalha na operação! Saldo insuficiente.')
        elif excedeu_limite:
            print('\nFalha na operação! Limite de saque excedido.')
        elif excedeu_saques:
            print('\nFalha na operação! Número máximo de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(type(extrato))
            numero_saques += 1
        else:
            print('Falha na operação! O valor informado é inválido.')
    
    elif opcao == 3:
        print('\n================ EXTRATO ================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print('_________________________________________')
        print(f'\nSaldo: R$ {saldo:.2f}') 
        print('=========================================')
    
    elif opcao == 0:
        break
    
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')

