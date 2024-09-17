usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido!")
else:
    print("Nome de usuário ou senha incorretos.")
