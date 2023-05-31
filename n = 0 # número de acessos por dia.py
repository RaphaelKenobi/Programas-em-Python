n = 0   # nÃºmero de acessos por dia
d = 0   # nÃºmero de dias
i = 0   # contador de vezes
soma = 0    # soma dos acessos
m = 0   # dia em que a meta foi atingida

d = int(input())  # usuario colocar o nÃºmero de dias

while (i < d):  # enquanto i for menor que d repete o laÃ§o
    n = int(input())
    i = 1 + i  # somador atÃ© i ser >= d
    if (soma < 1000000):
        m = m+1  # aumenta o nÃºmero de dias a cada vez que se repete o laÃ§o
        soma = soma + n  # altera o valor de viws
print(m)
