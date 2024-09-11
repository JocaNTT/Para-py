maior_numero = None

for num in range(1,6):
    numero = int(input(f"Digite o número {num}: "))
    
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

print(f"\nO maior número informado é: {maior_numero}\n")