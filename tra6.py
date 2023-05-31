def valor_devido(soma, x, horas_extra, horas_totais):
    if (horas_totais > 44):
        horas_extra += horas_totais - 44
    elif (horas_totais < 44):
        horas_extra += 0
    c = soma * x + horas_extra * (x/2)
    return c, horas_extra


def main():
    x = int(input())  # valor da hora
    y = int(input())  # número de dias

    if y >= 1 and y <= 7:
        soma = 0
        s = 0
        horas_extra = 0

    while y > 0:
        z = int(input())  # turnos
        s = 0
        while z > 0:
            he = int(input())  # horas de entrada
            hs = int(input())  # horas de saída
            s += hs - he  # descobrir o número de horas
            z -= 1
        y -= 1  # diminui o valor de dias

        if s <= 8:
            soma += s  # horas trabalhadas
        else:
            horas_extra += s - 8  # horas extras
            soma += s  # horas trabalhadas
        # calcula o salário considerando as horas trabalhadas e extras
    horas_totais = soma - horas_extra
    salario, horas_extra = valor_devido(soma, x, horas_extra, horas_totais)
    print("Horas trabalhadas: {}".format(soma))
    print("Horas extras: {}".format(horas_extra))
    print("Valor devido: {:.2f} R$".format(salario))


main()
