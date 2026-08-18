import random


# Cria o tabuleiro
def criar_tabuleiro(linhas, colunas):
    tabuleiro = []

    for i in range(linhas):
        linha = []

        for j in range(colunas):
            linha.append(".")

        tabuleiro.append(linha)

    return tabuleiro


# Cria as minas
def criar_minas(linhas, colunas, quantidade):
    minas = []

    # Cria todas as posições possíveis
    posicoes = []

    for linha in range(linhas):
        for coluna in range(colunas):
            posicoes.append([linha, coluna])

    # Escolhe uma posição aleatória para as minas
    for i in range(quantidade):
        mina = random.choice(posicoes)

        minas.append(mina)

        posicoes.remove(mina)

    return minas


# Mostra o tabuleiro
def mostrar_tabuleiro(tabuleiro):
    print()

    print("  ", end="")

    for coluna in range(len(tabuleiro[0])):
        print(coluna, end=" ")

    print()

    for linha in range(len(tabuleiro)):
        print(linha, end=" ")

        for coluna in range(len(tabuleiro[linha])):
            print(tabuleiro[linha][coluna], end=" ")

        print()

    print()


# Verifica se realmente existe uma mina la posição escolhida1
def tem_mina(minas, linha, coluna):

    for mina in minas:

        if mina[0] == linha and mina[1] == coluna:
            return True

    return False


# Conta as minas próximas da posição escolhida
def contar_minas(minas, linha, coluna):

    quantidade = 0

    for mina in minas:

        linha_mina = mina[0]
        coluna_mina = mina[1]

        if linha_mina >= linha - 1 and linha_mina <= linha + 1:
            if coluna_mina >= coluna - 1 and coluna_mina <= coluna + 1:

                if linha_mina != linha or coluna_mina != coluna:
                    quantidade = quantidade + 1

    return quantidade


#começo do jogo
print("==========================")
print("       CAMPO MINADO")
print("==========================")

linhas = int(input("Digite as linhas: "))
colunas = int(input("Digite as colunas: "))

print()
print("Escolha a dificuldade:")
print("1 - Fácil")
print("2 - Médio")
print("3 - Difícil")

dificuldade = int(input("Escolha: "))


# Define a dificuldade
if dificuldade == 1:
    quantidade_minas = 3
    vidas = 5
    dicas = 3

elif dificuldade == 2:
    quantidade_minas = 5
    vidas = 3
    dicas = 2

else:
    quantidade_minas = 7
    vidas = 2
    dicas = 1


# Cria o tabuleiro com as linhas e as colunas definidas pelo jogador
tabuleiro = criar_tabuleiro(linhas, colunas)
minas = criar_minas(linhas, colunas, quantidade_minas)

pontos = 0
casas_seguras = 0

total_casas_seguras = linhas * colunas - quantidade_minas


# Jogo
while vidas > 0:

    mostrar_tabuleiro(tabuleiro)

    print("Vidas:", vidas)
    print("Pontos:", pontos)
    print("Dicas:", dicas)

    print()
    print("1 - Jogar")
    print("2 - Usar dica")

    opcao = int(input("Escolha: "))


    # para começar o jogo
    if opcao == 1:

        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))

        # Verifica se a posição escolhida realmente existe
        if linha < 0 or linha >= linhas:
            print("Linha inválida!")
            continue

        if coluna < 0 or coluna >= colunas:
            print("Coluna inválida!")
            continue

        # Verifica se a casa já foi escolhida
        if tabuleiro[linha][coluna] != ".":
            print("Você já escolheu essa casa!")
            continue

        # Verifica se tem mina na posição escolhida
        if tem_mina(minas, linha, coluna):

            print("Você encontrou uma mina!")
            print("Você perdeu uma vida.")

            vidas = vidas - 1

            tabuleiro[linha][coluna] = "*"

        else:

            quantidade = contar_minas(minas, linha, coluna)

            tabuleiro[linha][coluna] = str(quantidade)

            pontos = pontos + 10
            casas_seguras = casas_seguras + 1

            print("Casa segura!")
            print("Existem", quantidade, "minas perto dessa casa.")
            print("Você ganhou 10 pontos.")

        # caso jogador ganhe
        if casas_seguras == total_casas_seguras:

            print()
            print("==========================")
            print("       VOCÊ VENCEU!")
            print("==========================")

            print("Pontos:", pontos)

            mostrar_tabuleiro(tabuleiro)

            break


    elif opcao == 2:

        if dicas > 0:

            linha = int(input("Digite a linha: "))
            coluna = int(input("Digite a coluna: "))

            if linha < 0 or linha >= linhas:
                print("Linha inválida!")
                continue

            if coluna < 0 or coluna >= colunas:
                print("Coluna inválida!")
                continue

            quantidade = contar_minas(minas, linha, coluna)

            print("Existem", quantidade, "minas perto dessa casa.")

            dicas = dicas - 1
            pontos = pontos - 20

        else:
            print("Você não tem mais dicas.")


    else:
        print("Opção inválida!")


# caso o jogador perca
if vidas == 0:

    print()
    print("==========================")
    print("       VOCÊ PERDEU!")
    print("==========================")

    print("Pontos:", pontos)

    # Mostra o local das minas no tabuleiro com um asterisco
    for mina in minas:
        tabuleiro[mina[0]][mina[1]] = "*"

    mostrar_tabuleiro(tabuleiro)