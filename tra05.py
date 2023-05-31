#### Raphael Pereira da Silva Piloneto###
######### 12221ECP001####################
##### 04-magic-the-gathering#########

# leitura dos dados de entrada
def main():
    orcamento = float(input())
    valor_booster = float(input())
    q_desejada = int(input())
# inicialização das variáveis
    soma = 0
    x = 0

# loop de valores
    while True:
        c_obtidas = int(input())
        soma += 1
        if (c_obtidas == 5 or c_obtidas == 3):
            x += 1
        if ((soma * valor_booster) + valor_booster > orcamento or x == q_desejada):
            total_gasto = soma * valor_booster
            restante = orcamento - total_gasto
        # valores
            print(f"ORCAMENTO: {orcamento:.2f} REAIS")
            print(f"VALOR DO BOOSTER: {valor_booster:.2f} REAIS")
            print(f"TOTAL GASTO: {total_gasto:.2f} REAIS")
            print(f"TOTAL RESTANTE: {restante:.2f} REAIS")
            print(f"QUANTIDADE DE BOOSTERS COMPRADOS: {soma}")
            print(
                f"QUANTIDADE DESEJADA DE CARTAS DA COR VERDE OU DA COR PRETA: {q_desejada}")
            print(
                f"QUANTIDADE OBTIDA DE CARTAS DA COR VERDE OU DA COR PRETA: {x}")
            if (x == q_desejada):
                print("JOAO CONSEGUIU MONTAR SEU NOVO DECK!")
            else:
                print("JOAO NAO CONSEGUIU MONTAR SEU NOVO DECK!")
            break


main()
