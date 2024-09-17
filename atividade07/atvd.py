frase = input("Digite uma frase: ")
caractere = input("Digite um caractere: ")

if len(caractere) == 1:
    if caractere in frase:
        print(f'O caractere "{caractere}" está presente na frase.')
    else:
        print(f'O caractere "{caractere}" não está presente na frase.')
else:
    print("Por favor, digite apenas um caractere.")
