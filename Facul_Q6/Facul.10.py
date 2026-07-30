numero1 = int(input())
numero2 = int(input())

n1_Primo = 0
n2_Primo = 0
soma = 0
soma_Primo = 0

if numero1 != 1 and numero1 != 0:
    for i in range(2, numero1):
        if numero1 % i == 0:
            n1_Primo = 1

if numero2 != 1 and numero2 != 0:
    for i in range(2, numero2):
        if numero2 % i == 0:
            n2_Primo = 1

if n1_Primo == 0 and n2_Primo == 0:
    soma = numero1 + numero2
    for i in range(2, soma):
        if soma % i == 0:
            soma_Primo = 1

if n1_Primo == 1:
    print(f"O numero {numero1} nao eh primo")
elif n2_Primo == 1:
    print(f"O numero {numero2} nao eh primo")
elif soma_Primo == 1:
    print(f"A soma de {numero1} e {numero2} nao eh um primo")
else:
    print(f"A soma de {numero1} e {numero2} eh um primo")