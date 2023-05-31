def main():
    MAPA = obter_mapa()  # Obtendo desenho do mapa
    qntd_sensores = int(input())  # Quantidade de sensores
    alcance_sensores = int(input())  # Alcance dos sensores
    # Posição inicial de cada sensor guardado em listas
    posicao_sensores = obter_posicao_sensores(qntd_sensores)
    loc_baus = []  # Lista que armazena as localizações dos baús, para evitar repetição na contagem

    for i in range(qntd_sensores):
        x_sensor, y_sensor = int(posicao_sensores[i][0]), int(
            posicao_sensores[i][1])  # Definindo posição inicial do sensor
        # Verificando se há baú na posição inicial do sensor
        loc_baus = verificar_posicao(MAPA, x_sensor, y_sensor, loc_baus)
        # Movendo e verificando se existem baús ao redor
        mover(alcance_sensores, MAPA, x_sensor, y_sensor, loc_baus, 'baixo')

        x_sensor, y_sensor = int(posicao_sensores[i][0]), int(
            posicao_sensores[i][1])
        loc_baus = verificar_posicao(MAPA, x_sensor, y_sensor, loc_baus)
        mover(alcance_sensores, MAPA, x_sensor, y_sensor, loc_baus, 'cima')

        x_sensor, y_sensor = int(posicao_sensores[i][0]), int(
            posicao_sensores[i][1])
        loc_baus = verificar_posicao(MAPA, x_sensor, y_sensor, loc_baus)
        mover(alcance_sensores, MAPA, x_sensor, y_sensor, loc_baus, 'direita')

        x_sensor, y_sensor = int(posicao_sensores[i][0]), int(
            posicao_sensores[i][1])
        loc_baus = verificar_posicao(MAPA, x_sensor, y_sensor, loc_baus)
        mover(alcance_sensores, MAPA, x_sensor, y_sensor, loc_baus, 'esquerda')

    if len(loc_baus) == 0:  # Se não existir nada na lista, não há baús encontrados
        print("Nenhum bau encontrado.")
    else:
        print(f"{len(loc_baus)} bau(s) encontrado(s).")


def obter_mapa():
    return [input().split() for _ in range(8)]


def obter_posicao_sensores(qntd_sensores):
    return [input().split() for _ in range(qntd_sensores)]


def mover(alcance_sensores, MAPA, x_sensor, y_sensor, loc_baus, direcao):
    for move in range(alcance_sensores):
        if direcao == 'baixo':
            if x_sensor + 1 < 8:
                x_sensor += 1
        elif direcao == 'cima':
            if x_sensor - 1 >= 0:
                x_sensor -= 1
        elif direcao == 'esquerda':
            if y_sensor - 1 >= 0:
                y_sensor -= 1
        elif direcao == 'direita':
            if y_sensor + 1 < 8:
                y_sensor += 1
        if MAPA[x_sensor][y_sensor] == 'o':
            break
        loc_baus = verificar_posicao(MAPA, x_sensor, y_sensor, loc_baus)
    return x_sensor, loc_baus


def verificar_posicao(MAPA, X_SENSOR, Y_SENSOR, LOC_BAUS):
    if MAPA[X_SENSOR][Y_SENSOR] == 'x':
        # Verificando se, caso haja baú naquela posição, ele já não tenha sido encontrado previamente
        if [X_SENSOR, Y_SENSOR] not in LOC_BAUS:
            LOC_BAUS.append([X_SENSOR, Y_SENSOR])
    return LOC_BAUS
