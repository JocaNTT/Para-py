media = 33.5
acima_ou_igual = 0
abaixo = 0

for num in range(1,8):
    temperatura = float(input(f"Digite a temperatura {num}: "))
    
    if temperatura >= media:
        acima_ou_igual += 1
    else:
        abaixo += 1

print(f"\nTemperaturas iguais ou acima de {media}°C: {acima_ou_igual}")
print(f"Temperaturas abaixo de {media}°C: {abaixo}\n")