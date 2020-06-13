# Fonte: https://www.thehuxley.com/problem/1094
#TODO: Finalizar
total_votantes = 0
total_a = 0
total_b = 0
total_c = 0
total_brancos = 0
total_nulos = 0
total_validos = 0
total_invalidos = 0

while True:
    sessao = int(input())

    if sessao == 0:
        break

    votos_a = int(input())
    total_a += votos_a

    votos_b = int(input())
    total_b += votos_b
    votos_c = int(input())
    total_c += votos_c

    votos_brancos = int(input())
    total_brancos += votos_brancos

    votos_nulos = int(input())
    total_nulos += votos_nulos
    votos_invalidos = votos_brancos + votos_nulos
    total_invalidos += votos_invalidos

    votos_validos = votos_a + votos_b + votos_c
    total_validos += votos_validos

    votos_invalidos = votos_brancos + votos_nulos
    total_invalidos += votos_invalidos

    total_votantes += votos_validos + votos_invalidos


print(f"Numero de votantes: {total_votantes}")

print(f"Total A: {total_a}")
print(f"Total B: {total_b}")
print(f"Total C: {total_c}")

print(f"Brancos: {total_brancos}")
print(f"Nulos: {total_nulos}")

print(f"Validos: {total_validos}")

mais_votado = ""
mais_votado_votos = ""

if total_a > total_b:
    mais_votado = "A"
    mais_votado_votos = total_a
else:
    mais_votado = "B"
    mais_votado_votos = total_b

if mais_votado_votos < total_c:
    mais_votado = "C"
    mais_votado_votos = total_c

print(f"Candidato mais votado: {mais_votado}")

eleicao_valida = None

if total_validos > total_invalidos:
    eleicao_valida = True
else:
    eleicao_valida = False

print(f"Eleicao valida? {eleicao_valida}")

segundo_turno = None

if mais_votado_votos > (1 / 2) * total_validos:
    segundo_turno = False
else:
    segundo_turno = True

print(f"Segundo turno? {segundo_turno}")
    