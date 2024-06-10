import os
os.system('cls' if os.name == 'nt' else 'clear')

lista_1 = ["C","C++","Python","Java"]
lista_2 = ["PHP","SQL","Visual Basic"]
lista_3 = ["d","a","c","b","e"]
lista_4 = [5, 4, 7, 1, 9]
lista_5 = [True,False]
lista_12 = lista_1 + lista_2
lista_13 = lista_1 + lista_3
lista_14 = lista_1 + lista_4
lista_15 = lista_1 + lista_5
lista_5.append(True)
print(lista_5.pop(0))
print(lista_1[0])
print(lista_2[0])
print(lista_12)
print(lista_13)
print(lista_14)
print(lista_15)
print(lista_5)
lista_5.sort()
print(lista_5)
lista_5.reverse()
print(lista_5)