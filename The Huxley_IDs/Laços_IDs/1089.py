def soma_S():
    numero = int(input())
    termos = 1
    soma = 0
    serie = ""

    if numero != 0:
        while  termos <= numero:
            if termos < numero:
                serie += (f"{termos}/{termos*3} + ")
            elif termos == numero:
                serie += (f"{termos}/{termos*3}")
            soma += termos/(termos*3)
            termos += 1
        print(serie)
        print(f"{soma:.2f}")
    else:
        print(f"{numero:.2f}")

soma_S()