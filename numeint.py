def calcular_soma_digitos(numero):
    soma = 0
    for digito in str(numero):
        soma += int(digito)
    return soma


# Entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Cálculo da soma dos dígitos
soma_digitos = calcular_soma_digitos(numero)

# Impressão do resultado
print(soma_digitos)
