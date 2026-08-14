import random

MINA = "*"
OCULTO = "."
TESOURO = "$"
SEGURA = "X"

# Criar o tabuleiro
def criar_tabuleiro(linhas, colunas):
    tabuleiro = []

    for i in range(linhas):
        linha = []

        for j in range(colunas):
            linha.append(OCULTO)

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


# Verificar se tem mina
def tem_mina(minas, linha, coluna):
    for mina in minas:

        if mina[0] == linha and mina[1] == coluna:
            return True

    return False


# Programa
print("======================")
print("     CAMPO MINADO")
print("======================")

linhas = int(input("Digite as linhas: "))
colunas = int(input("Digite as colunas: "))
quantidade_minas = int(input("Digite a quantidade de minas: "))

tabuleiro = criar_tabuleiro(linhas, colunas)

minas = criar_minas(linhas, colunas, quantidade_minas)

# Criar o tesouro
while True:
    tesouro_linha = random.randint(0, linhas - 1)
    tesouro_coluna = random.randint(0, colunas - 1)

    if not tem_mina(minas, tesouro_linha, tesouro_coluna):
        break


vidas = 3
pontos = 0
casas_descobertas = 0

casas_seguras = linhas * colunas - quantidade_minas

while vidas > 0:

    mostrar_tabuleiro(tabuleiro)

    print("❤️ Vidas:", vidas)
    print("⭐ Pontos:", pontos)

    linha = int(input("Escolha a linha: "))
    coluna = int(input("Escolha a coluna: "))

    # Verificar se a posição existe
    if linha < 0 or linha >= linhas or coluna < 0 or coluna >= colunas:
        print("❌ Essa posição não existe!")
        continue

    
    if tabuleiro[linha][coluna] != OCULTO:
        print("⚠️ Você já escolheu essa casa!")
        continue

    
    if tem_mina(minas, linha, coluna):

        print(" BOOM!")
        print("Você encontrou uma mina!")

        vidas = vidas - 1

        print("Você perdeu uma vida!")

        tabuleiro[linha][coluna] = MINA

    else:

        # Verificar tesouro
        if linha == tesouro_linha and coluna == tesouro_coluna:

            print(" VOCÊ ENCONTROU O TESOURO!")
            print("+50 pontos!")

            pontos = pontos + 50

            tabuleiro[linha][coluna] = TESOURO

        else:

            print("Casa segura!")
            print("+10 pontos!")

            pontos = pontos + 10

            tabuleiro[linha][coluna] = SEGURA

        casas_descobertas = casas_descobertas + 1

    
    if casas_descobertas == casas_seguras:

        print()
        print("======================")
        print("      🎉 VITÓRIA!")
        print("======================")
        print("Você encontrou todas as casas seguras!")
        print("⭐ Pontuação:", pontos)

        mostrar_tabuleiro(tabuleiro)

        break


if vidas == 0:

    print()
    print("======================")
    print("      DERROTA")
    print("======================")
    print("Você ficou sem vidas!")
    print(" Pontuação:", pontos)

    for mina in minas:
        tabuleiro[mina[0]][mina[1]] = MINA

    # Mostrar o tesouro
    tabuleiro[tesouro_linha][tesouro_coluna] = TESOURO

    mostrar_tabuleiro(tabuleiro)