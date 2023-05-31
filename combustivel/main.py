T = float(input())  # T=tempo
Vm = float(input())  # Vm=velocidade media

distancia = Vm * T  # fÃ³rmula para descobrir distÃ¢ncia
combustivel = distancia/12

print("{:.3f}".format(combustivel))
