mes = int(input())
ano = int(input())

if mes in (1, 3, 5, 7, 8, 10, 12):
    print("31")

elif mes in (4, 6, 9, 11):
    print("30")

elif mes == 2:
    if ano % 4 == 0 and not (ano % 100 == 00 and not ano % 400 == 00):
        print("29")
    else:
        print("28")