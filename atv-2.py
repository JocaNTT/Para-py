numeros = []

for num in range(1,9):
    numero = float(input(f"Digite o número {num}: "))
    numeros.append(numero)

quantidade_negativos = 0
soma_positivos = 0

for num in numeros:
    if num < 0:
        quantidade_negativos += 1
    elif num > 0:
        soma_positivos += num

print(f"\nQuantidade de números negativos: {quantidade_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")