# ajudinha do chatGPT
def multiplos_5():
    limite_inf, limite_sup = input().split()
    limite_inf, limite_sup = int(limite_inf), int(limite_sup)

    multiplos = ""
    ultimo = limite_sup - (limite_sup % 5)

    if limite_inf > limite_sup:
        limite_inf, limite_sup = limite_sup, limite_inf

    for num in range(limite_inf, limite_sup + 1):
        if num % 5 == 0:
            multiplos += str(num)
            
            if num != ultimo:
                multiplos += "|"

    print(multiplos)

multiplos_5()