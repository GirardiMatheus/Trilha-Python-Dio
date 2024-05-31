menu = """
####Bem vindo ao DIO-Bank####

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

Digite alguma das opções acima para realizar a operação!

####Bem vindo ao DIO-Bank####
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques= 3

while True:
    opcao = input(menu)
    
    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor - 0:
            saldo += valor
            saldo == valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif opcao == "S":
        valor = float(input("Informe o valor de saque: "))
        
        exedeu_saldo = valor > saldo
        
        exedeu_limite = valor > limite
        
        exedeu_saques = numero_saques >= limite_saques
        
        if exedeu_saldo:
            print("Operação falhou! Vcê ão tem saldo suficiente.")
        
        elif exedeu_limite:
            print("Operação falhou! O valor do saque exedeu o limite.")
        
        elif exedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")

        
    elif opcao == "E":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================")
    
    elif opcao == "Q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
