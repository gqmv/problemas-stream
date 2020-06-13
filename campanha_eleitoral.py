# Fonte: https://www.thehuxley.com/problem/931?locale=pt_BR

class Candidato():
    def __init__(self, nome, qtd_midias):
        self.nome = nome
        self.qtd_midias = qtd_midias
        self.valor_gasto = 0

TABELA_PRECOS = {"internet": 3000, "revista": 750, "outdoor": 1500, "radiofm": 500, "radioam": 300, "tvregular": 1200, "tvnobre": 2000}

while True:
    entrada = input()

    if entrada == "FIM":
        break

    nome, qtd_midias = entrada.split()

    candidato = Candidato(nome, int(qtd_midias))

    for midia in range(candidato.qtd_midias):
        entrada = input()

        if entrada == "tv":
            horario = int(input())
            if horario > 20:
                candidato.valor_gasto += TABELA_PRECOS["tvnobre"]
            else:
                candidato.valor_gasto += TABELA_PRECOS["tvregular"]
            continue

        if entrada == "radio":
            tipo = input()
            candidato.valor_gasto += TABELA_PRECOS[entrada + tipo]
            continue

        candidato.valor_gasto += TABELA_PRECOS[entrada]

    print(f"{candidato.nome}: {candidato.valor_gasto:.2f}")

        
