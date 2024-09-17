  
numero = int(input("Digite um número: "))

if numero % 2 == 0 :
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é impar.')

if numero > 0:
    print(f'O número {numero} é positivo.')
elif numero < 0:
    print(f'O número {numero} é negativo.')
else:
    print(f'O número {numero} é zero.')
   
