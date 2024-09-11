for num in range(1, 51):
    saida = ""
    
    if num % 3 == 0:
        saida += "Fizz"
    if num % 5 == 0:
        saida += "Buzz"
    
    if saida == "":
        saida = str(num)
    
    print(f"Número {num}: {saida}")