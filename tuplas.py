import os
os.system('cls' if os.name == 'nt' else 'clear')

mi_tuple = (1,"dos", [3.33,"cuatro"], (5.0, 6))

print(mi_tuple)
print(mi_tuple[0])
print(mi_tuple[2][2])

lista1 = list(mi_tuple)
print(lista1)

#Umpacking de tuplas (desempaqueto de tuplas)
a, b, c, d = mi_tuple
print(a)
print(b)
print(c)
print(d)

#tupla de pi, e, gravedad
tuplaConst = (3.1416, 2.7182, 9.81)
pi,ex,gr=tuplaConst
print(f"pi={pi}, ex={ex}, gravedad={gr}")
