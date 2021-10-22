def funkcja(a_list, b_list):
    c_list = []
    if len(a_list) <= len(b_list):
        for i in range(0, len(a_list)-1):
            c_list.append(b_list[i])
            c_list.append(a_list[i])
    else:
        for i in range(0, len(a_list)-1):
            c_list.append(b_list[i])
            c_list.append(a_list[i])
    return c_list

lista1 = [2, 4, 6, 8]
lista2 = [1, 3, 5, 7]
print(len(lista2))
print(len(lista1))
lista3 = funkcja(lista1, lista2)
print(lista3)