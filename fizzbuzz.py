
VALOR_MAXIMO = 100

for numero in range(1, VALOR_MAXIMO + 1):
    saida = ""

    if numero % 2 == 0:
        saida += "Fizz"
    if numero % 3 == 0:
        saida += "Buzz"
    if numero % 5 == 0:
        saida += "Zyzz"
    

    if saida == "":
        saida = numero

    print(saida)
