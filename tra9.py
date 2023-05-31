###### Raphael Pereira da Silva Piloneto######
############# 12221ECP001#####################
########### caça ao tesouro###################

def explorar_campo(campo, posicao_inicial, alcance):
    linhas = len(campo)
    colunas = len(campo[0])

    direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for direcao in direcoes:
        linha_atual, coluna_atual = posicao_inicial
        for _ in range(alcance):
            linha_atual += direcao[0]
            coluna_atual += direcao[1]

            if linha_atual < 0 or linha_atual >= linhas or coluna_atual < 0 or coluna_atual >= colunas:
                break

            elif campo[linha_atual][coluna_atual] == 'x':
                return True  # Baú encontrado

    return False  # Baú não encontrado


def main():
    campo = []  # campo inicialmente vazio até que seja dada as coordenadas pelo usuario
    for _ in range(8):  # faz a entrada de linhas e acrescenta em colunas para formar uma matriz 8x8 ou a critério do usuario
        linha = input()
        campo.append(list(linha))

    # numero de sensores a serem percorridos pelo drone
    num_sensores = int(input())
    alcance_sensores = int(input())  # numero de sensores

    sensores = []
    for _ in range(num_sensores):
        # leitura de número feito em espaços
        posicao = tuple(map(int, input().split()))
        sensores.append(posicao)

    bau_encontrado = False
    for sensor in sensores:
        posicao_inicial = (sensor[0], sensor[1])
        if explorar_campo(campo, posicao_inicial, alcance_sensores):
            bau_encontrado = True
            break

    if bau_encontrado:
        print("1 bau encontrado.")
    else:
        print("Nenhum bau encontrado.")


main()
