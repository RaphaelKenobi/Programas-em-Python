
def main():
    M = cria_matriz()
    l, c = dimensoes(M)
    print("")

    print("Matriz: ")
    imprime_matriz(M, l, c)
    print("")

    diagonal_secundaria(M, l, c)
    print("")

    print(f"É simétrica? {simetria(M,l,c)}")
    print("")

    P = int(input("Quer criar uma segunda matriz? (NÂO = 0 e SIM = 1) "))
    print("")
    if (P == 1):

        M2 = cria_matriz()
        l2, c2 = dimensoes(M2)
        print("")

        print("Matriz: ")
        imprime_matriz(M2, l2, c2)
        print("")

        somadematrizes(M, M2, l, c)
        print("")

        print(f"São multiplicáveis? {sao_mult(M,M2,l,c)}")
        print("")


def cria_matriz():
    l = int(input("Quantas linhas? "))
    c = int(input("Quantas colunas? "))
    M = []
    for i in range(l):
        linha = []
        for j in range(c):
            numero = int(input(f"Entre com o valor {i+1}x{j+1}: "))
            linha.append(numero)
        M.append(linha)
    return M


def imprime_matriz(M, l, c):
    for i in range(l):
        for j in range(c):
            if (j < c - 1):
                print(M[i][j], end=',\t')
            else:
                print(M[i][j])


def diagonal_secundaria(M, l, c):
    lista = []
    if (l > 1) and (l > 1):
        for i in range(len(M)):
            ds = M[i][len(M)-1-i]
            lista.append(ds)
        print(f"Diagonal secundária = {lista}")
    else:
        return False


def dimensoes(M):
    l = len(M)
    c = len(M[0])
    return l, c


def somadematrizes(M, M2, l, c):
    if (dimensoes(M) != dimensoes(M2)):
        print("Não é possível somar matrizes de dimensões diferentes")
        return False
    else:
        MS = []
        for i in range(l):
            linha = []
            for j in range(c):
                soma = M[i][j] + M2[i][j]
                linha.append(soma)
            MS.append(linha)
    print("Soma das matrizes:")
    imprime_matriz(MS, l, c)
    return MS


def sao_mult(M, M2, l, c):
    if (l == c):
        return True
    else:
        return False


def transposta(M, l, c):
    MT = [[0]*l for i in range(c)]
    for i in range(l):
        for j in range(c):
            MT[i][j] = M[j][i]
    print("Transposta da Matriz: ")
    imprime_matriz(MT, l, c)
    return MT


def simetria(M, l, c):
    T = transposta(M, l, c)
    if (T == M):
        return True
    else:
        return False


main()
