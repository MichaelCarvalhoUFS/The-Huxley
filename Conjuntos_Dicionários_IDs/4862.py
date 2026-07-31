def final(alunos_total, futebol, corrida, volei, natacao):
    print("Todos os competidores:")
    lista_total = sorted(alunos_total)
    for i in range(len(lista_total)):
        separador = "-" if i < len(lista_total) - 1 else ""
        print(f"{lista_total[i]}{separador}", end="")
    print()
    
    print("Nao inscritos em futebol:")
    lista_nao_futebol = sorted(alunos_total - futebol)
    for i in range(len(lista_nao_futebol)):
        separador = "-" if i < len(lista_nao_futebol) - 1 else ""
        print(f"{lista_nao_futebol[i]}{separador}", end="")
    print()
    
    print("Inscritos em corrida ou natacao:")
    lista_corrida_natacao = sorted(corrida | natacao)
    for i in range(len(lista_corrida_natacao)):
        separador = "-" if i < len(lista_corrida_natacao) - 1 else ""
        print(f"{lista_corrida_natacao[i]}{separador}", end="")
    print()

alunos_total = set()
futebol = set()
corrida = set()
volei = set()
natacao = set()

for _ in range(4):
    inscricao = input().split("(")
    esporte_alunos = []
    for i in inscricao:
        alunos = []
        esporte_alunos.append(i.lower())

    esporte = [esporte_alunos[0]]
    alunos = esporte_alunos[1].split(",")
    
    for i in range(len(alunos)):
        alunos[i] = alunos[i].replace(")", "")

    for x in alunos:
        if esporte[0] == "futebol":
            futebol.add(x.upper())
            alunos_total.add(x.upper())
        elif esporte[0] == "corrida":
            corrida.add(x.upper())
            alunos_total.add(x.upper())
        elif esporte[0] == "volei":
            volei.add(x.upper())
            alunos_total.add(x.upper())
        elif esporte[0] == "natacao":
            natacao.add(x.upper())
            alunos_total.add(x.upper())

final(alunos_total, futebol, corrida, volei, natacao)