preco_original = float(input("Digite o preço original do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))

total = preco_original * quantidade

if quantidade > 10:
    total *= 0.90
    print(f'O valor total a pagar é: R$ {total:.2f}')
else: 
    print('A quantidade comprada não é maior que 10. O preço permanece o mesmo.')