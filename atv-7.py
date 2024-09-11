a = int(input("Digite o primeiro número inteiro positivo (a): "))
b = int(input("Digite o segundo número inteiro positivo (b): "))

contador_multiplos = 0

if a > b:
    a, b = b, a

for i in range(a, b + 1):
    if i % 7 == 0 and i % 11 == 0:
        contador_multiplos += 1

print(f"\nTotal de números entre {a} e {b} que são múltiplos de 7 e 11: {contador_multiplos}")