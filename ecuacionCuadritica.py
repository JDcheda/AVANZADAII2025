#Crear una función para resolver una ecuación cuadrática.
# a*x^2 + b*x + c = 0
# a, b, c
def discriminante(a, b, c):
    discrim = (b**2)-(4*a*c)
    return discrim
# Crear una función para resolver una ecuación cuadrática.
# a*x^2 + b*x + c = 0
# a, b, c
def discriminante(a, b, c):
    # Calcula el valor del discriminante (b**2)-(4*a*c)
    discrim = (b**2) - (4*a*c)
    return discrim

def raices(a, b, c):
    # Calcula las raíces de la ecuación cuadrática
  #raiz1=(-b + sqrt(discrim))/(2*a)
  #raiz2=(-b - sqrt(discrim))/(2*a)
  raiz1=(-b + (discrim**.5))/(2*a)
  raiz2=(-b - (discrim**.5))/(2*a)
  cero = -b/(2*a)
  return raiz1,raiz2,cero

    enter code here

print('Calculo de raices')
a=float(input('a: '))
b=float(input('b: '))
c=float(input('c: '))
disc=discriminante(a,b,c)

if disc < 0:
  print("No hay raices positivas")

elif sdiscrimin == 0:
  print('Solo existe una raiz')
  print(raices(cero))
  
else:
  print("La raices son: ")    
  print(raices(a,b,c))# Crear una función para resolver una ecuación cuadrática.
# a*x^2 + b*x + c = 0
# a, b, c

def discriminante(a, b, c):
    # Calcula el valor del discriminante (b**2)-(4*a*c)
    discrim = (b**2) - (4*a*c)
    return discrim

def raices(a, b, c):
    # Calcula las raíces de la ecuación cuadrática
    discriminante_valor = discriminante(a, b, c)
    if discriminante_valor < 0:
        print("No hay raices positivas")
    elif discriminante_valor == 0:
        # Solo existe una raiz (x = -b / (2*a))
        print('Solo existe una raiz')
        print(f'La raiz es: {-b/(2*a)}')
    else:
        # La ecuación tiene dos raíces
        raiz1 = (-b + math.sqrt(discriminante_valor)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante_valor)) / (2*a)
        print("La raices son: ")
        print(f'Raiz 1: {raiz1:.2f}')
        print(f'Raiz 2: {raiz2:.2f}')


print('Calculo de raices')
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

discriminante_valor = discriminante(a, b, c)

if discriminante_valor < 0:
    print("No hay raices positivas")

elif discriminante_valor == 0:
    print('Solo existe una raiz')
    print(raices(a, b, c))

else:
    print("La raices son: ")
    print(raices(a, b, c))
