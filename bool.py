import os
os.system('cls' if os.name == 'nt' else 'clear')

mibool=True

#Comparaciones
a = 6 > 5
b = 30 == 15*3
print(not(mibool == a and mibool != b))