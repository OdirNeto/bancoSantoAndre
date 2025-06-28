menu = '''
======menu=====

[1] Extrato
[2] Depositar
[3] Sacar
[0] Sair

===============

Por favor digite o numero da opção desejada:
'''

saldo = 0
limitePorSaque = 500
limiteDeSaques = 3
extrato = ""
saquesRealizados = 0


print("Bem Vindo ao Banco Santo André")


while True:
    
    opcao = input(menu)

    if opcao == "1":
        print("\n------------------------EXTRATO------------------------")
        print("Você não realizou nenhuma transação até o momento" if not extrato else extrato)
        print(f"\nSeu saldo atual é de R${saldo:.2f}")
        print("---------------------------------------------------------")
    
    
    elif opcao == "2":
        valor = float(input("\nInforme o valor do deposito: R$"))
    
        if valor >= 1:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"     
    
            print(f"\nA quantia de R${valor:.2f} foi depositada com sucesso. Seu saldo atual é de R${saldo:.2f}.")      
    
        else:
            print("O deposito não pode ser concluído pois o valor informado é inválido")
    
    
    elif opcao == "3":
    
        if saquesRealizados >= limiteDeSaques:
           print("""
                 Por motivo de segurança você atingiu o numero máximo de saques por dia.
                                     Selecione outra opção do menu:
                  """)
    
        else:
            print(f"""
                  Por motivos de segurança só são permitidos 3 saques por dia, com o valor máximo de R$500.00 por saque.
                                        Até o momento você efetuou {saquesRealizados} saques hoje.
                  """)
            valor = float(input("\nInforme o valor que deseja sacar: R$"))
    
            if valor > limitePorSaque:
                print("""
                      Para a sua segurança o valor limite por saque é de $R500.00. Tente um valor menor.
                      """)
    
            elif valor <= 0:
                print("""
                O valor informado é invalido. Tente um outro valor.
                """)
    
            elif valor > saldo:
                print("""
                               Infelizmente não há saldo suficiente na sua conta.
                Fale com o seu gerente e ative o cheque especial para te ajudar em momentos como este.
                """)
    
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                saquesRealizados += 1
                print(f"""
                      Saque realizado com sucesso. Seu saldo atual é de R${saldo:.2f}
                      """)
    
    
    elif opcao == "0":
        print("""
                                Santo André
            Cuidamos do seu dinheiro para você cuidar do resto.
              """)
        break
    
    
    else:
        print("Opção inválida, por favor selecione uma opção a seguir:")