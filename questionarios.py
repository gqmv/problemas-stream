# Fonte: https://www.thehuxley.com/problem/1999
num_questoes = int(input())

while (True):
    gabarito = input().split()

    if len(gabarito) == num_questoes:
        break
    else:
        print("Gabarito de tamanho errado. Entre com o novo gabarito:")


while True:
    questoes_certas = 0
    entrada = input()

    if entrada == "sair":
        break

    gabarito_estudante = entrada.split()

    if len(gabarito_estudante) != num_questoes:
        print("Tamanho da resposta diferente do tamanho do gabarito.")
        continue
    
    for i in range(num_questoes):
        if gabarito_estudante[i] == gabarito[i]:
            questoes_certas += 1

    percentual_acertos = questoes_certas / num_questoes * 100

    print(f"Percentual de acertos: {percentual_acertos:.1f}")
    
