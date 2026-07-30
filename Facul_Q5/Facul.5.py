def elevador():
    sensor, capacidade = input().split()
    sensor = int(sensor)
    capacidade = int(capacidade)
    excedencia = "N"
    total_pessoas = 0
    
    while sensor > 0:
        saida, entrada = input().split()
        saida = int(saida)
        entrada = int(entrada)

        total_pessoas -= saida
        total_pessoas += entrada
        sensor -= 1

        if total_pessoas > capacidade:
            excedencia = "S"
    print(excedencia)

elevador()