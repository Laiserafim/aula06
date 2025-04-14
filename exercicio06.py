nota1= float(input("Primeira nota: "))
while nota1 < 0 or nota1 > 10:
    print("Nota incorreta. Digite novamente")
    nota1 = float(input("Digite a primeira nota novamente: "))

nota2= float(input("segunda nota: "))
while nota2 < 0 or nota2 > 10:
    print("Nota incorreta. Digite novamente")
    nota2 = float(input("Digite a segunda nota novamente: "))

media = (nota1 + nota2)/2
print(f"A média é : {media}")
