# Fonte: https://www.thehuxley.com/problem/484?locale=pt_BR
animais = {}
# {"cobra": [soma_pesos, qtd, [paises_origem]]}

while True:
    tipo = input().lower()
    peso = float(input())
    pais_origem = input().lower()

    if animais.get(tipo) != None:
        animais[tipo][0] += peso
        animais[tipo][1] += 1
        animais[tipo][2].append(pais_origem)
    else:
        animais[tipo] = [peso, 1, [pais_origem]]

    entrada = input().lower()
    
    if entrada == "parar":
        break

try:
    qtd_macacos = animais["macaco"][1]
except KeyError:
    qtd_macacos = 0
try:
    qtd_tigres = animais["tigre"][1]
    soma_pesos_tigres = animais["tigre"][0]
    peso_medio_tigres = soma_pesos_tigres / qtd_tigres
except KeyError:
    peso_medio_tigres = 0

try:
    cobras_venezuelanas = 0
    for pais in animais["cobra"][2]:
        if pais == "venezuela":
            cobras_venezuelanas += 1
except KeyError:
    cobras_venezuelanas = 0


print(qtd_macacos)
print(f"{peso_medio_tigres:.2f}")
print(cobras_venezuelanas)





