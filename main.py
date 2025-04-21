import os
import random
from colorama import Fore

# Variáveis globais
jogar_novamente = "s"
numero_jogadas = 0
vez_do_jogador = 2  # 1 = CPU, 2 = Jogador
maximo_jogadas = 9
vencedor = "n"
tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Função para exibir o tabuleiro
def exibir_tabuleiro():
    os.system("cls")
    print("    0   1   2")
    for i in range(3):
        print(f"{i}:  {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]}")
        if i < 2:
            print("   -----------")
    print("Jogadas: " + Fore.GREEN + str(numero_jogadas) + Fore.RESET)

# Jogada do jogador
def jogada_jogador():
    global numero_jogadas, vez_do_jogador

    if vez_do_jogador == 2 and numero_jogadas < maximo_jogadas:
        try:
            linha = int(input("Digite a linha (0, 1 ou 2): "))
            coluna = int(input("Digite a coluna (0, 1 ou 2): "))

            while tabuleiro[linha][coluna] != " ":
                print("Essa posição já foi jogada!")
                linha = int(input("Digite a linha (0, 1 ou 2): "))
                coluna = int(input("Digite a coluna (0, 1 ou 2): "))

            tabuleiro[linha][coluna] = "X"
            vez_do_jogador = 1
            numero_jogadas += 1
        except:
            print("Linha ou coluna inválida!")
            os.system("pause")

# Jogada da CPU (aleatória)
def jogada_cpu():
    global numero_jogadas, vez_do_jogador

    if vez_do_jogador == 1 and numero_jogadas < maximo_jogadas:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)

        while tabuleiro[linha][coluna] != " ":
            linha = random.randint(0, 2)
            coluna = random.randint(0, 2)

        tabuleiro[linha][coluna] = "O"
        vez_do_jogador = 2
        numero_jogadas += 1

# Verifica vitória
def verificar_vitoria():
    simbolos = ["X", "O"]
    for simbolo in simbolos:
        # Verifica linhas
        for linha in tabuleiro:
            if linha.count(simbolo) == 3:
                return simbolo

        # Verifica colunas
        for col in range(3):
            if tabuleiro[0][col] == simbolo and tabuleiro[1][col] == simbolo and tabuleiro[2][col] == simbolo:
                return simbolo

        # Verifica diagonais
        if tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo:
            return simbolo
        if tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo:
            return simbolo

    return "n"

# Reinicia o jogo
def reiniciar_jogo():
    global tabuleiro, numero_jogadas, vez_do_jogador, vencedor
    tabuleiro = [[" ", " ", " "] for _ in range(3)]
    numero_jogadas = 0
    vez_do_jogador = 2
    vencedor = "n"

# Loop principal
while jogar_novamente.lower() == "s":
    os.system("cls")

    while True:
        exibir_tabuleiro()
        jogada_jogador()
        jogada_cpu()
        exibir_tabuleiro()
        vencedor = verificar_vitoria()

        if vencedor != "n" or numero_jogadas >= maximo_jogadas:
            break

    print(Fore.RED + "FIM DE JOGO" + Fore.RESET)
    if vencedor in ["X", "O"]:
        print(Fore.YELLOW + f"Vencedor: {vencedor}" + Fore.RESET)
    else:
        print(Fore.YELLOW + "Empate!" + Fore.RESET)

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == "s":
        reiniciar_jogo()
    else:
        print("Obrigado por jogar!")
        break