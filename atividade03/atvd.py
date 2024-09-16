idade = int(input("Digite sua idade: "))

if idade >=18:
    print("Maior de idade.")
else:
    print("Menor de idade.")
    exit()

habilitacao = int(input("Você possui habilitação?(digite 1 para SIM e 2 para NÃO)"))

if habilitacao == 1:
    print ("Possui habilitação")
elif habilitacao == 2:
    print ("Não possui habilitação")
else:
    print ("Insira uma resposta valida")