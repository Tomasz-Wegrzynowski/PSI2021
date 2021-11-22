a_list = [1,2,3,4,5,6]
b_list = [5,8,9,10,21,32,1,33]

def funkcja(a_list,b_list):
    
    lista = []
    for i,v in enumerate(a_list):
        if i % 2 == 0:
            lista.append(v)
            print(lista)
    for i,v in enumerate(b_list):
        if i % 2 == 1:
            lista.append(v)
            print(lista)


funkcja(a_list,b_list)

