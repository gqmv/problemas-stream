# Fonte: https://www.thehuxley.com/problem/960
# O arbitro virtual do The Huxley apresenta comportamento
# duvidoso ao julgar este problema.

class Aluno():
    def __init__(self, matricula, nome, nota):
        self.matricula = matricula
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.__str__()


def get_nota(obj):
    return obj.nota

# Obtencao de entrada
num_alunos = int(input())

alunos_nota_vermelha = []
alunos_nota_verde = []
soma_notas = 0

for _ in range(num_alunos):
    entradas = input().split(sep="-")
    matricula = int(entradas[0])
    nome = entradas[1]
    nota = float(entradas[2])
    aluno = Aluno(matricula, nome, nota)
    
    soma_notas += aluno.nota

    if aluno.nota < 7:
        alunos_nota_vermelha.append(aluno)
    else:
        alunos_nota_verde.append(aluno)

alunos_nota_verde.sort(key=get_nota)
alunos_nota_vermelha.sort(key=get_nota)
media_geral = soma_notas / num_alunos

print("Alunos abaixo da media:")

for aluno in alunos_nota_vermelha:
    print(f"Matricula: {aluno.matricula} Nome: {aluno.nome} Nota: {aluno.nota:.1f}")


print("Alunos iguais ou acima da media:")
for aluno in alunos_nota_verde:
    print(f"Matricula: {aluno.matricula} Nome: {aluno.nome} Nota: {aluno.nota:.1f}")

print(f"Media = {media_geral:.2f}")




