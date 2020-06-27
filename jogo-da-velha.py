def obter_coordenadas(numero):
    if numero >= 0 and numero <= 3:
        return (0, numero - 1)

    if numero >= 4 and numero <= 6:
        return (1, numero - 4)

    if numero >= 7 and numero <= 9:
        return (2, numero - 7)

    raise ValueError


def imprimir_tabuleiro(array_tabuleiro):
    for linha in array_tabuleiro:
        for elemento in linha:
            print(f"  {elemento}  |", end="")

        print()

        print("------------------")

        print()


def checar_vitoria(array_tabuleiro):
    for i in range(len(array_tabuleiro)):
        # Checagem horizontal
        if "X" not in array_tabuleiro[i] and 3 * i + 1 not in array_tabuleiro[i] and 3 * i + 2 not in array_tabuleiro[i] and 3 * i + 3 not in array_tabuleiro[i]:
            return "O"

        if "O" not in array_tabuleiro[i] and 3 * i + 1 not in array_tabuleiro[i] and 3 * i + 2 not in array_tabuleiro[i] and 3 * i + 3 not in array_tabuleiro[i]:
            return "X"

    # Checagem vertical
    for i in range(3):
        if array_tabuleiro[0][i] == array_tabuleiro[1][i] and array_tabuleiro[1][i] == array_tabuleiro[2][i]:
            if array_tabuleiro[0][i] != 1 or array_tabuleiro[0][1] != 2 or array_tabuleiro[0][1] != 3:
                return array_tabuleiro[0][i]

    
    # Checagem diagonal
    if array_tabuleiro[0][0] == array_tabuleiro[1][1] and array_tabuleiro[1][1] == array_tabuleiro[2][2]:
        return array_tabuleiro[0][0]

    if array_tabuleiro[0][2] == array_tabuleiro[1][1] and array_tabuleiro[1][1] == array_tabuleiro[2][0]:
        return array_tabuleiro[0][2]



if __name__ == "__main__":

    pontuacao_x = 0
    pontuacao_o = 0

    #Loop Geral
    while True:
        array_tabuleiro = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        proximo_jogador = "X"
        jogadas = 0
        #Loop do jogo
        while True:
            imprimir_tabuleiro(array_tabuleiro)


            try:
                numero_jogada = int(input(f"Onde deseja jogar? ({proximo_jogador})"))
                x, y = obter_coordenadas(numero_jogada)

                if array_tabuleiro[x][y] != numero_jogada:
                    raise ValueError

            except (ValueError, TypeError):
                print("Valor invalido.")
                continue

            array_tabuleiro[x][y] = proximo_jogador

            if proximo_jogador == "X":
                proximo_jogador = "O"
            else:
                proximo_jogador = "X"

            vencedor = checar_vitoria(array_tabuleiro)

            if vencedor == "X":
                print("X Venceu!")
                pontuacao_x += 1
                break

            if vencedor == "O":
                print("O Venceu!")
                pontuacao_o += 1
                break
            

            jogadas += 1

            if jogadas >= 9:
                print("Empate!")
                break

        imprimir_tabuleiro(array_tabuleiro)

        print("Pontuacao:")
        print(f"X: {pontuacao_x}")
        print(f"O: {pontuacao_o}")

        print("Quer jogar novamente?")
        resposta = input("Digite 'S' para sim e qualquer outra coisa para nao.")

        if resposta.lower() != "s":
            break




            