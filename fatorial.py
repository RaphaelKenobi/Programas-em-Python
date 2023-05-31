def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

# Função principal


def main():
    n = int(input("Digite o valor de n: "))
    fatorial = calcular_fatorial(n)
    print(fatorial)


# Chamando a função principal
main()
