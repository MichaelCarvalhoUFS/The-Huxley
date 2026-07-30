cpf = input().split(".")
cpf2 = cpf[2].split("-")

for i in range(len(cpf) -1):
    print(cpf[i])
for i in range(len(cpf2)):
    print(cpf2[i])