import random

# Criar o tabuleiro
def criar_tabuleiro(linhas, colunas):
    tabuleiro = []

    for i in range(linhas):
        linha = []

        for j in range(colunas):
            linha.append(".")

        tabuleiro.append(linha)

    return tabuleiro


# Criar as minas
def criar_minas(linhas, colunas, quantidade):
    minas = []

    while len(minas) < quantidade:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)

        if [linha, coluna] not in minas:
            minas.append([linha, coluna])

    return minas


# Mostrar o tabuleiro
def mostrar_tabuleiro(tabuleiro):
    print()

    for i in range(len(tabuleiro)):
        print(i, end=" ")

        for j in range(len(tabuleiro[i])):
            print(tabuleiro[i][j], end=" ")

        print()

    print()


# Verificar se existe uma mina
def tem_mina(minas, linha, coluna):
    for mina in minas:
        if mina[0] == linha and mina[1] == coluna:
            return True

    return False


# Programa principal

print("=== CAMPO MINADO ===")

linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))
quantidade_minas = int(input("Digite a quantidade de minas: "))

tabuleiro = criar_tabuleiro(linhas, colunas)
minas = criar_minas(linhas, colunas, quantidade_minas)

vidas = 3
pontos = 0
casas_seguras = 0

while vidas > 0:

    mostrar_tabuleiro(tabuleiro)

    print("Vidas:", vidas)
    print("Pontos:", pontos)

    linha = int(input("Digite a linha: "))
    coluna = int(input("Digite a coluna: "))

    # Verificar se a posição existe
    if linha < 0 or linha >= linhas or coluna < 0 or coluna >= colunas:
        print("Posição inválida!")
        continue

    # Verificar se já foi escolhida
    if tabuleiro[linha][coluna] != ".":
        print("Você já escolheu essa posição!")
        continue

    # Verificar se encontrou uma mina
    if tem_mina(minas, linha, coluna):

        print("Você encontrou uma mina!")
        print("Você perdeu uma vida.")

        vidas = vidas - 1
        tabuleiro[linha][coluna] = "*"

    else:

        print("Casa segura!")

        tabuleiro[linha][coluna] = "X"
        pontos = pontos + 10
        casas_seguras = casas_seguras + 1

    # Verificar vitória
    if casas_seguras == linhas * colunas - quantidade_minas:

        print()
        print("=== VOCÊ VENCEU ===")
        print("Pontuação:", pontos)

        mostrar_tabuleiro(tabuleiro)

        break


if vidas == 0:

    print()
    print("=== FIM DE JOGO ===")
    print("Você perdeu!")
    print("Pontuação:", pontos)

    # Mostrar onde estavam as minas
    for mina in minas:
        tabuleiro[mina[0]][mina[1]] = "*"

    mostrar_tabuleiro(tabuleiro)