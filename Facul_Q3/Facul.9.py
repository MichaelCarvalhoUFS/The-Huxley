partida1 = int(input())
partida2 = int(input())
partida3 = int(input())
partida4 = int(input())
partida5 = int(input())
partida6 = int(input())

pontos_total = partida1 + partida2 + partida3 + partida4 + partida5 + partida6

if pontos_total > 100:
    print("Classificado")
else:
    print("Eliminado")