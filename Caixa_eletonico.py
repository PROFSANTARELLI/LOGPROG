def exibir_menu():
    print("\n=== Caixa Eletrônico ===")
    print("1 - Consultar Saldo")
    print("2 - Sacar Dinheiro")
    print("3 - Sair")

def caixa_eletronico():
    saldo = 1000  # Saldo inicial

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"\nSeu saldo atual é: R$ {saldo:.2f}")
        
        elif opcao == "2":
            saque = float(input("\nDigite o valor do saque: R$ "))

            if saque > saldo:
                print(f"\nSaldo insuficiente! Você tem apenas R$ {saldo:.2f}")
            
            elif saque <= 0:
                print("\nValor inválido! Digite um valor maior que zero.")
            
            else:
                saldo -= saque
                print(f"\nSaque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")

        elif opcao == "3":
            print("\nObrigado por usar o caixa eletrônico!")
            break  # Sai do loop
        else:
            print("\nOpção inválida! Tente novamente.")

caixa_eletronico()
