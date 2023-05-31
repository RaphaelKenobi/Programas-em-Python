def calcular_melhor_combinacao_desconto(d1, vpd, d2, vpd2, d3, vpd3, lista1):
    a = len(lista1)  # percorre o tamanho da lista
    melhor_combinacao = [0, 0, 0]  # retorna valores para print
    maior_desconto = 0  # variavel para receber o desconto

    for i in range(a):  # percorre valores para desconto mais externo d1
        if lista1[i] <= vpd:  # condiÃ§Ã£o do cupom1
            continue
        for j in range(a):  # percorre valores para desconto mais externo d2
            if i == j or lista1[j] <= vpd2:  # condiÃ§Ã£o cupom 2
                continue
            for k in range(a):  # percorre valores para desconto mais externo d3
                if k == j or k == i or lista1[k] < vpd3:  # condiÃ§Ã£o cupom2
                    continue
                desconto_total = 0  # variavel do desconto total
                if vpd < lista1[i]:
                    desconto_total += d1
                if vpd2 < lista1[j]:
                    desconto_total += min((d2/100) * lista1[j], vpd2)
                if vpd3 < lista1[k]:
                    desconto_total += (d3/100) * lista1[k]
                if desconto_total > maior_desconto:
                    maior_desconto = desconto_total
                    melhor_combinacao = [i+1, j+1, k+1]

    return melhor_combinacao

# print das saidas


def imprimir_melhor_combinacao(melhor_combinacao):
    print("Cupom 1:", melhor_combinacao[0])
    print("Cupom 2:", melhor_combinacao[1])
    print("Cupom 3:", melhor_combinacao[2])

# funÃ§Ã£o principal para receber dados do usuario


def main():
    d1 = float(input())  # desconto do cupom1
    vpd = float(input())  # valor para desconto2
    d2 = float(input())  # desconto do cupom2
    vpd2 = float(input())  # valor para desconto2
    d3 = float(input())  # desconto do cupom3
    vpd3 = float(input())  # valor para desconto3
    n = int(input())  # nÃºmero de compras
    lista1 = []  # lista com valores de compra

    for _ in range(n):  # atribuir valores a lista de compras
        c = float(input())
        lista1.append(c)

    melhor_combinacao = calcular_melhor_combinacao_desconto(
        d1, vpd, d2, vpd2, d3, vpd3, lista1)  # chamada da funÃ§Ã£o
    imprimir_melhor_combinacao(melhor_combinacao)


main()
