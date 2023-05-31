def calcular_distancia(x1, y1, x2, y2):
    distancia = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distancia


def main():
    x1 = float(input("Digite a coordenada x do primeiro ponto: "))
    y1 = float(input("Digite a coordenada y do primeiro ponto: "))
    x2 = float(input("Digite a coordenada x do segundo ponto: "))
    y2 = float(input("Digite a coordenada y do segundo ponto: "))

    distancia = calcular_distancia(x1, y1, x2, y2)

    if distancia >= 10:
        print("longe")
    else:
        print("perto")


main()
