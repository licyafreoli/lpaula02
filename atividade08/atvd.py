frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

if palavra in frase:
    print(f'A palavra "{palavra}" está presente na frase.')
else:
    print(f'A palavra "{palavra}" não está presente na frase.')
