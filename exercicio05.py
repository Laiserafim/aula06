tentativa = 1
pin= 123456
resposta= "Excesso de tentativas, login bloqueado!"

while tentativa <= 3:
    senha = int(input("Senha: "))
    if senha == pin:
        resposta="Login efetuado com sucesso! "
        break
    tentativa += 1

print(resposta)
