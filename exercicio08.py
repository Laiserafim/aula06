n = int(input("Digite o número"))

for x in range(1,n+1):
    for y in range (1, x+1, 1):
        print(x, end=" ")
    print()