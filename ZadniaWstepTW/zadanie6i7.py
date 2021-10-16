lista = list(range(1, 11))
print(lista)
lista2 = lista[5::]
lista = lista[0:5]
print(lista)
print(lista2)
lista = [0] + lista + lista2
print(lista)
lista3 = sorted(lista, reverse = True)
print(lista3)