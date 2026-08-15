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

    while len(minas) < quantidade:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)

        if [linha, coluna] not in minas:
            minas.append([linha, coluna])

    return minas


# Mostra o tabuleiro
def mostrar_tabuleiro(tabuleiro):
    print()

    # Número das colunas
    print("  ", end="")

    for i in range(len(tabuleiro[0])):
        print(i, end=" ")

    print()

    # Tabuleiro
    for i in range(len(tabuleiro)):
        print(i, end=" ")

        for j in range(len(tabuleiro[i])):
            print(tabuleiro[i][j], end=" ")

        print()

    print()


# Verifica se existe uma mina
def tem_mina(minas, linha, coluna):
    for mina in minas:

        if mina[0] == linha and mina[1] == coluna:
            return True

    return False


# Conta as minas ao redor
def contar_minas(minas, linha, coluna):
    quantidade = 0

    for mina in minas:

        diferenca_linha = abs(mina[0] - linha)
        diferenca_coluna = abs(mina[1] - coluna)

        if diferenca_linha <= 1 and diferenca_coluna <= 1:
            if diferenca_linha != 0 or diferenca_coluna != 0:
                quantidade = quantidade + 1

    return quantidade


# Escolha da dificuldade
print("=== CAMPO MINADO ===")
print()
print("Escolha a dificuldade:")
print("1 - Fácil")
print("2 - Médio")
print("3 - Difícil")

dificuldade = int(input("Escolha: "))

linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

if dificuldade == 1:
    quantidade_minas = 3
    vidas = 5

elif dificuldade == 2:
    quantidade_minas = 5
    vidas = 3

else:
    quantidade_minas = 8
    vidas = 2


# Cria o jogo
tabuleiro = criar_tabuleiro(linhas, colunas)
minas = criar_minas(linhas, colunas, quantidade_minas)

pontos = 0
casas_seguras = 0
dicas = 3

casas_necessarias = linhas * colunas - quantidade_minas


# Começa o jogo
while vidas > 0:

    mostrar_tabuleiro(tabuleiro)

    print("Vidas:", vidas)
    print("Pontos:", pontos)
    print("Dicas restantes:", dicas)

    print()
    print("1 - Jogar")
    print("2 - Usar dica")

    opcao = int(input("Escolha uma opção: "))

    # Jogar
    if opcao == 1:

        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))

        # Verifica posição
        if linha < 0 or linha >= linhas or coluna < 0 or coluna >= colunas:

            print("Posição inválida!")
            continue

        # Verifica se já foi escolhida
        if tabuleiro[linha][coluna] != ".":

            print("Você já escolheu essa posição!")
            continue

        # Verifica mina
        if tem_mina(minas, linha, coluna):

            print("Você encontrou uma mina!")
            print("Você perdeu uma vida.")

            vidas = vidas - 1

            tabuleiro[linha][coluna] = "*"

        else:

            quantidade = contar_minas(minas, linha, coluna)

            print("Casa segura!")

            # Mostra quantas minas existem perto
            if quantidade == 0:
                tabuleiro[linha][coluna] = "0"
                print("Não existem minas próximas.")

            else:
                tabuleiro[linha][coluna] = str(quantidade)
                print("Existem", quantidade, "mina(s) próxima(s).")

            pontos = pontos + 10
            casas_seguras = casas_seguras + 1

        # Verifica vitória
        if casas_seguras == casas_necessarias:

            print()
            print("=== VOCÊ VENCEU ===")
            print("Pontuação:", pontos)

            mostrar_tabuleiro(tabuleiro)

            break


    # Usar dica
    elif opcao == 2:

        if dicas > 0:

            linha = int(input("Digite a linha para receber a dica: "))
            coluna = int(input("Digite a coluna para receber a dica: "))

            if linha < 0 or linha >= linhas or coluna < 0 or coluna >= colunas:

                print("Posição inválida!")

            elif tabuleiro[linha][coluna] != ".":

                print("Essa posição já foi escolhida!")

            else:

                quantidade = contar_minas(minas, linha, coluna)

                print("Existem", quantidade, "mina(s) perto dessa posição.")

                dicas = dicas - 1
                pontos = pontos - 5

                print("Você gastou uma dica e perdeu 5 pontos.")

        else:

            print("Você não possui mais dicas!")


    else:

        print("Opção inválida!")


# Se perder todas as vidas
if vidas == 0:

    print()
    print("=== FIM DE JOGO ===")
    print("Você perdeu!")
    print("Pontuação:", pontos)

    # Mostra todas as minas
    for mina in minas:
        tabuleiro[mina[0]][mina[1]] = "*"

    mostrar_tabuleiro(tabuleiro)