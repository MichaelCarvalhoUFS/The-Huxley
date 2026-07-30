def vantagem(percentual_Candidato, percentual_Concorrente, votos):
    maiorVantagem = 0

    for i in range(votos):
        if (percentual_Candidato[i] - percentual_Concorrente[i]) > maiorVantagem:
            maiorVantagem = (percentual_Candidato[i] - percentual_Concorrente[i])
    print(f"{maiorVantagem:.2f}")

votos = int(input())
percentual_Candidato = []
percentual_Candidato += input().split()
percentual_Candidato = [float(x) for x in percentual_Candidato]

percentual_Concorrente = []
percentual_Concorrente += input().split()
percentual_Concorrente = [float(x) for x in percentual_Concorrente]
vantagem(percentual_Candidato, percentual_Concorrente, votos)

#percentual_concorrente ou percentual_candidato = [float(x) for x in input().split()]5