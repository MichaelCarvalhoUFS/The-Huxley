
def interseccao(lista1, lista2):
    lst_final = []
    
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j] and lista1[i] not in lst_final:
                lst_final.append(lista1[i])
                
    lst_final.sort()
    return lst_final