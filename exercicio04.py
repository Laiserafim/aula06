n1 = int(input("Digite o primeiro número: "))
n2  = int (input("Digite o segundo número"))
divisao=0

while n2 ==0:
    print(("Número inválido."))
    n2 = int(input("Digite um número diferente de Zero "))

divisao = n1/n2
print(divisao)