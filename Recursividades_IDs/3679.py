def inversa():
    numero = int(input())
    
    if numero == 0:
        return
    else:
        inversa()
        print(numero)
    
inversa()
