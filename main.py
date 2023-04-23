n = int(input("Digite um número inteiro: "))

for i in range(1, n+1):
    if i**2 <= n**2:
        print(i**2)
    else:
        break