def votacao():
    voto = int(input())
    alibaba = 0
    alcapone = 0
    votos_Brancos = 0
    votos_nulos = 0
    vencedor = 0
    percentual_Alibaba = 0
    percentual_Alcapone = 0
    votos_validos = 0

    while voto != -1:
        if voto == 83:
            alibaba += 1
        elif voto == 93:
            alcapone += 1
        elif voto == 0:
            votos_Brancos += 1
        else:
            votos_nulos +=1
        
        voto = int(input())
    
    if alibaba > alcapone:
        vencedor = 83
    elif alibaba < alcapone:
        vencedor = 93
    votos_validos = alibaba + alcapone + votos_Brancos
    percentual_Alibaba = (alibaba / votos_validos) * 100
    percentual_Alcapone = (alcapone / votos_validos) * 100


    print(alibaba)
    print(alcapone)
    print(votos_Brancos)
    print(votos_nulos)
    print(vencedor)
    print(f"{percentual_Alibaba:.2f}")
    print(f"{percentual_Alcapone:.2f}")

votacao()