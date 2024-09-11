import random

def lancar_dados():
    contagem = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for _ in range(1,11):
        numero = random.randint(1, 6)
        contagem[numero] += 1
    
    return contagem

resultado = lancar_dados()

print(f"\nContagem dos números sorteados:")
for numero, vezes in resultado.items():
    print(f"Número {numero}: {vezes} vez(es)")