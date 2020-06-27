class Cliente():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f'{self.nome}, tem {self.idade} anos.'

    def __repr__(self):
        return self.nome

    @property
    def idade_por_10(self):
        return self.idade/10
        

gabriel = Cliente(nome="Gabriel", idade=525)

print(gabriel)

lista = [gabriel]

print(lista)