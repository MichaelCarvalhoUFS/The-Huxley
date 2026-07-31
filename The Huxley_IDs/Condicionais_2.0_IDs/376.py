quant_livros = int(input())
quant_alunos = int(input())

if (quant_alunos // quant_livros) <= 8:
    print("A")

elif (quant_alunos // quant_livros) <= 12:
    print("B")

elif (quant_alunos // quant_livros) <= 18:
    print("C")

elif (quant_alunos // quant_livros) > 18:
    print("D")