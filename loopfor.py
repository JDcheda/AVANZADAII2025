import os
os.system('cls' if os.name == 'nt' else 'clear')


# #ciclo for
# #for i in range(10):
#     #print(i)

# #range(inicio, fin, incremento)
# #for i in range(2, 22,2):
#     #print(i)

# #ciclo con lista
# #lista=["uno","dos","tres","cuatro","cinco"]
# #for item in lista:
#     #print(item)

# #ciclo para tupla
# #tupla=("uno","dos","tres","cuatro","cinco")
# #for item in tupla:
#     #print(item)

# #ciclo con diccionario
# #diccionario={"curso":"Python Total",
#              "clase":"Ciclos",
#              "tema":"For",
#              "duracion":"trimestre",
#              "profesor":"Luis Teruel"}
# for item in diccionario:
#     print(item)

# for llave in diccionario:
#     print(llave, ":", diccionario[llave])


# #Invertir el orden de una lista
# for item in reversed(lista):
#     print(item)
# #ciclo con conjunto
# #conjunto={"uno","dos","tres","cuatro","cinco"}
# #for item in conjunto:
#     #print(item)

# #ciclo con string
# #cadena="hola"
# #for item in cadena:
#     #print(item)

#Programa para pedir al usuario que le pida que tabla de multiplicar desea obtener y mostrarla
#tabla=int(input("Ingrese la tabla de multiplicar que desea obtener: "))
#for i in range(1,11):
    #print(tabla,"x",i,"=",tabla*i)

#Calcular el factorial con for
numero=int(input("Ingrese un numero: "))
factorial=1
for i in range(1,numero+1):
    factorial*=i
print("El factorial de",numero,"es",factorial)