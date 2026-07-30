numero = int(input())

numero_IP = 0
numero_PN = 0

if numero > 0:
    numero_PN = "POSITIVO"
elif numero < 0:
    numero_PN = "NEGATIVO"
elif numero == 0:
    numero_PN = "NULO"

if numero % 2 == 0:
    numero_IP = "PAR"
elif numero % 2 != 0:
    numero_IP = "IMPAR"

if numero == 0:
    numero_IP = ""

print(numero_PN ,numero_IP)