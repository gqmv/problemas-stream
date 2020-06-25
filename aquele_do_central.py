# Fonte: https://www.thehuxley.com/problem/2469

class Cliente():
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []

ross = Cliente("Ross")
chandler = Cliente("Chandler")
monica = Cliente("Monica")
phoebe = Cliente("Phoebe")
joey = Cliente("Joey")
outros = []

clientes = [chandler, phoebe, joey, monica,ross]



TIPOS_AMIGOS = {"Suco": ross, "Cafe": chandler, "Refrigerante": monica, "Cerveja": joey, "Cha": phoebe}

qtd_pedidos = int(input())

for i in range(qtd_pedidos):
    comida, tipo = input().split()
    cliente = TIPOS_AMIGOS.get(tipo, outros)

    try:
        pedidos = cliente.pedidos
    except AttributeError:
        pedidos = cliente
        
    pedidos.append(comida)

pedidos_amigos = 0

for cliente in clientes:
    pedidos_amigos += len(cliente.pedidos)


if pedidos_amigos != 0:

    for cliente in clientes:
        if len(cliente.pedidos) > 0:
            print(f'{cliente.nome}:')
            for pedido in cliente.pedidos:
             print(f'-{pedido}')
        else:
            print(f'{cliente.nome} não pediu nada.')
        
        print()


    if len(outros) > 0:
        print("Outros Clientes:")
        for pedido in outros:
            print(f'-{pedido}')
else:
    print("Nenhum dos meus amigos veio, não vou trabalhar hoje.")

