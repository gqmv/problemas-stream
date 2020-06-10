# Fonte: https://www.thehuxley.com/problem/348
numero_romano = list(input())

numero_romano.reverse()

romano_para_arabico = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}



numero_arabico = [romano_para_arabico[numero_romano[0]]]
numero_final = numero_arabico[0]
for i in range(1,len(numero_romano)):
    numero_arabico.append(romano_para_arabico[numero_romano[i]])

    if numero_arabico[i] >= numero_arabico[i - 1]:
        numero_final += numero_arabico[i]
    else:
        numero_final -= numero_arabico[i]

print(numero_final)