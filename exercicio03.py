i=1
n= int(input("Quantidade de alunos: "))
soma=0
while i <= n:
    nota = float(input("Digite a nota do aluno: "))
    soma = soma + nota
    i = i + 1
media = soma / n
print(f"A média da sala é {media}")


