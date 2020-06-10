# Fonte https://www.thehuxley.com/problem/2253?locale=pt_BR
# TODO: Ordenar saidas de forma alfabetica, seguindo especificacoes do problema
tamanho_a, tamanho_b = input().split()
tamanho_a = int(tamanho_a)
tamanho_b = int(tamanho_b)

selecionados_a, selecionados_b = input().split()
selecionados_a = int(selecionados_a)
selecionados_b = int(selecionados_b)

a = input().split()

a = list(map(int, a))

b = input().split()

b = list(map(int, b))

a.sort()
b.sort(reverse=True)

if a[selecionados_a - 1] < b[selecionados_b - 1]:
    print("YES")
else:
    print("NO")
