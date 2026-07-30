participantes = int(input())
amigo_secreto = dict()

for i in range(participantes):
    linha_participantes = input().split()
    participante = linha_participantes[0]
    amigo_secreto[participante] = [linha_participantes[1], linha_participantes[2], linha_participantes[3]]


    teste = input().split()
    nome_participante = teste[0]
    nome_participante in amigo_secreto