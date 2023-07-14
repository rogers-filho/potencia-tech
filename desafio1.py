menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do Depósito: R$ "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido!")

    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: R$ "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou: Saldo insuficiente!")

        elif excedeu_limite:
            print("Operação falhou: O valor informado é maior que o limite de saque")

        elif excedeu_saque:
            print("Operação falhou: O limite de saques diários foi excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else: 
            print("Operação falhou: O valor inserido é inválido")

    elif opcao == "e":
        print("\n==================== EXTRATO ====================")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida. Insira uma operação válida.")