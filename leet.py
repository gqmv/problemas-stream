# Fonte: https://www.thehuxley.com/problem/1165?locale=pt_BR

def traduzir_letra(letra):
    letra = letra.lower()

    tabela_traducoes = {"a": "@", "e": "3", "i": "1", "o": "0", "t": "7", "s": "5"}
    
    return tabela_traducoes.get(letra, letra)



if __name__ == "__main__":
    NUMEROS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    palavra_normal = list(input())

    saida = ""
    palavra_leet = ""
    qtd_alteradas = 0
    for letra in  reversed(palavra_normal):
        if letra in NUMEROS:
            palavra_leet = "numeros"
            qtd_alteradas = 0
            break

        letra_leet = traduzir_letra(letra)
        palavra_leet += letra_leet
        
        if letra_leet != letra:
            qtd_alteradas += 1

    for letra in palavra_leet:
        print(letra, end="")
    print()
    print(qtd_alteradas)




