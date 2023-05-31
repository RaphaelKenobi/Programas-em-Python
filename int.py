def imprimir_numeros_impares(n):
    contador = 0
    numero = 1
    while contador < n:
        if numero % 2 != 0:
            print(numero)
            contador += 1
        numero += 1


# Entrada do usuário
n = int(input("Digite o valor de n: "))

# Impressão dos números ímpares

imprimir_numeros_impares(n)
