import random
import time
 
OCULTA = "."
MINA = "*"
BANDEIRA = "B"
ARQUIVO_RANKING = "ranking.txt"
 
 

 
def criar_matriz(linhas, colunas, valor):
    return [[valor for _ in range(colunas)] for _ in range(linhas)]
 
 
def posicionar_minas(linhas, colunas, qtd_minas):
    minas = criar_matriz(linhas, colunas, False)
    colocadas = 0
    while colocadas < qtd_minas:
        l, c = random.randint(0, linhas - 1), random.randint(0, colunas - 1)
        if not minas[l][c]:
            minas[l][c] = True
            colocadas += 1
    return minas
 
 
def contar_vizinhas(minas, linha, coluna):
    total = 0
    for dl in (-1, 0, 1):
        for dc in (-1, 0, 1):
            l, c = linha + dl, coluna + dc
            if (dl, dc) != (0, 0) and 0 <= l < len(minas) and 0 <= c < len(minas[0]):
                if minas[l][c]:
                    total += 1
    return total
 
 

 
def mostrar_tabuleiro(visivel):
    print("   " + " ".join(str(c) for c in range(len(visivel[0]))))
    for i, linha in enumerate(visivel):
        print(i, "|", " ".join(linha))
 
 

def revelar(visivel, minas, linha, coluna):
    if not (0 <= linha < len(minas) and 0 <= coluna < len(minas[0])):
        return
    if visivel[linha][coluna] != OCULTA:
        return
 
    vizinhas = contar_vizinhas(minas, linha, coluna)
    visivel[linha][coluna] = str(vizinhas) if vizinhas > 0 else " "
 
    if vizinhas == 0:
        for dl in (-1, 0, 1):
            for dc in (-1, 0, 1):
                revelar(visivel, minas, linha + dl, coluna + dc)
 
 
def venceu(visivel, minas):
    for l in range(len(minas)):
        for c in range(len(minas[0])):
            if not minas[l][c] and visivel[l][c] == OCULTA:
                return False
    return True
 
 

 
def carregar_ranking():
    try:
        with open(ARQUIVO_RANKING, "r") as arquivo:
            return [float(linha) for linha in arquivo.readlines()]
    except FileNotFoundError:
        return []
 
 
def salvar_ranking(tempos):
    melhores = sorted(tempos)[:5]
    with open(ARQUIVO_RANKING, "w") as arquivo:
        for tempo in melhores:
            arquivo.write(f"{tempo:.2f}\n")
    return melhores
 
 
def mostrar_ranking(melhores):
    print("\n Ranking dos melhores tempos:")
    for pos, tempo in enumerate(melhores, start=1):
        print(f"{pos}º lugar - {tempo:.2f} segundos")
 
 

def jogar():
    print("=== CAMPO MINADO ===")
    linhas = int(input("Linhas: "))
    colunas = int(input("Colunas: "))
    qtd_minas = int(input("Quantidade de minas: "))
 
    minas = posicionar_minas(linhas, colunas, qtd_minas)
    visivel = criar_matriz(linhas, colunas, OCULTA)
 
    inicio = time.time()
 
    while True:
        mostrar_tabuleiro(visivel)
        l = int(input("Linha: "))
        c = int(input("Coluna: "))
 
        if minas[l][c]:
            print("\n Você pisou em uma mina! Fim de jogo.")
            break
 
        revelar(visivel, minas, l, c)
 
        if venceu(visivel, minas):
            tempo_final = time.time() - inicio
            mostrar_tabuleiro(visivel)
            print(f"\n Você venceu em {tempo_final:.2f} segundos!")
 
            tempos = carregar_ranking()
            tempos.append(tempo_final)
            melhores = salvar_ranking(tempos)
            mostrar_ranking(melhores)
            break
 
 
if __name__ == "__main__":
    jogar()
 