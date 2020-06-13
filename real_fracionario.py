# Fonte: https://www.thehuxley.com/problem/344?locale=pt_BR

def encontrar_primos(max):
    prime = [True for i in range(max + 1)]
    p = 2
    while (p * p <= max):

        # Se prime[p] nao for alterado, entao p e primo.
        if (prime[p] == True):

            # Define todos os multiplos de p como False.
            for i in range(p * 2, max + 1, p):
                prime[i] = False
        p += 1
        # Define 0 e 1 como False, visto que nao sao primos.
    prime[0] = False
    prime[1] = False

    prime_numbers = []
    for i in range(len(prime)):
        if prime[i] == True:
            prime_numbers.append(i)
        
    return prime_numbers
    

def simplifica(numerador, denominador):
    primos = encontrar_primos(numerador)

    divisores = []
    for primo in primos:
        if numerador % primo == 0 and denominador % primo == 0:
            divisores.append(primo)
    
    for primo in divisores:
        numerador = numerador / primo
        denominador = denominador / primo
    
    return numerador, denominador

    

numero_real = float(input())

numerador = int(numero_real * 100)

denominador = 100

if numerador != 0:

    negativo = False

    if numerador < 0:
        negativo = True
        numerador *= -1

    while True:
        novo_numerador, novo_denominador = simplifica(numerador, denominador)
        if novo_numerador == numerador and novo_denominador == denominador:
            if negativo:
                numerador = -1 * novo_numerador
            else:
                numerador = novo_numerador
            denominador = novo_denominador
            break

        numerador = int(novo_numerador)
        denominador = int(novo_denominador)

else:
    numerador = 0
    denominador = 1


print(f"{numerador}/{denominador}")



