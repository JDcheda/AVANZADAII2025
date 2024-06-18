import os
os.system('cls' if os.name == 'nt' else 'clear')

# i=0
# while i<10:
#     print(i)
#     i+=1

# print("Ciclo controlado por banderin")

# while True:
#     entrada = input()
#     if entrada.upper == 'S':
#         break
#     print("Escribiste: ", entrada)

print("Ciclo controlado por banderin 2")
bandera = True
while bandera != False:
    bandera = input("Ingrese S para terminar: ")
    print(bandera.upper())
    salir = bandera.upper()
    if salir == 'S':
        bandera = False
        print("saliste del ciclo")

