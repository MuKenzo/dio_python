menu = """

[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

Digite a opção desejada:
"""

saldo = 0
limite = 500
extrato = ''
número_saques = 0
LIMITE_SAQUES = 3

while True:

    opção = input(menu)

    if opção == 'd':
        depósito = float(input('Informe o valor que deseja depositar: '))
        
        if depósito > 0:
            saldo += depósito
            extrato += f'Depósito: R$ {depósito:.2f}\n'
        
        else:
            print('Operação falhou! O valor informado é inválido.')
    
    elif opção == 's':
        saque = float(input('Informe o valor que deseja sacar: '))

        excedeu_saldo = saque > saldo

        excedeu_limite = saque > limite

        excedeu_saques = número_saques >= LIMITE_SAQUES
            
        if excedeu_saldo:
            print('Operação falhou! Você não possui saldo suficiente.')
        
        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite.')
        
        elif excedeu_saques:
            print('Operação falhou! Número máximo de sques excedido.')
        
        elif saque > 0:
            saldo -= saque
            extrato = f'Saque: R$ {saque:.2f}\n'
            número_saques += 1
    
    elif opção == 'e':
        print('\n============ EXTRATO ============')
        (print('Não foram realizadas movimentações.' if not extrato else extrato))
        print(f'Saldo = R$ {saldo:.2f}')
        print('===================================')
    
    elif opção == 'q':
        break
        
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada: ")