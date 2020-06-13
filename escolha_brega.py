# Fonte: https://www.thehuxley.com/problem/1149?locale=pt_BR

entrada = input().split()
horas = int(input())
diamantes_arthur, diamantes_luiz, diamantes_pedro = map(int, entrada)

maximo = (diamantes_arthur + diamantes_luiz + abs(diamantes_arthur - diamantes_luiz)) / 2
maximo = (maximo + diamantes_pedro + abs(maximo - diamantes_pedro)) / 2

print(int(maximo * horas))