ano = int(input())

if ano % 4 == 0 and not (ano % 100 == 00 and not ano % 400 == 00):
        print("BISSEXTO")
else:
    print("NAOBISSEXTO")