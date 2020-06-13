num_casos = int(input())

for caso in range(num_casos):
    entrada = input().split()
    x1, y1, x2, y2 = map(int, entrada)

    distancia = (((x1 - x2)** 2) + ((y1 - y2)** 2))** (1 / 2)
    
    print(f'{distancia:.2f}')