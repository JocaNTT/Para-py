n = int(input("Digite um número inteiro: "))

soma_divisores = 0

for num in range(1, n):
    if n % num == 0:
        soma_divisores += num

if soma_divisores == n:
    print(f"{n} é um número perfeito! (soma de seus divisores é igual a ele)")
else:
    print(f"{n} não é um número perfeito.")