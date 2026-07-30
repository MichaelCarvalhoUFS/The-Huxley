#gemini q fez
def interseccao(lista1, lista2):
    lst_final = []
    
    # Passa por cada elemento da lista1
    for i in range(len(lista1)):
        # Passa por cada elemento da lista2
        for j in range(len(lista2)):
            # Se forem iguais e ainda não estiverem na lista final, adiciona
            if lista1[i] == lista2[j] and lista1[i] not in lst_final:
                lst_final.append(lista1[i])
                
    # Ordena a lista em ordem crescente antes de retornar
    lst_final.sort()
    return lst_final


"""def interseccao(lst1, lst2):
	if len(lst1) < len(lst2):
	    lst1, lst2 = lst2, lst1
    lst_final = []
    for i in range(len(lst1)-1):
        for j in range(len(lst2)-1):
            if lst1[i] == lst2[j] and lst1[i] not in lst_final:
                lst_final.append(lst1[i])
    return lst_final

lista1 = eval(input())
lista2 = eval(input())
resultado = interseccao(lista1, lista2)
if isinstance(resultado, list):
	print(resultado)
else:
	print("Erro. Voce deve devolver uma lista")
	"""