print ("Ejercicio 1")
print('Resolviendo el ejercicio :)')
deposito = float(input("Introduce tu deposito inicial: "))
print (deposito)

interes = 1.04
deposito1 = deposito * (interes)
print("Pasado el primer año usted habrá acumulado:" + str(round(deposito1, 2)))
deposito2 = deposito * (interes)**2
print("Pasado el segundo año usted habrá acumulado:" + str(round(deposito2, 2)))
deposito3 = deposito * (interes)**3
print("Pasado el tercer año usted habrá acumulado:" + str(round(deposito3, 2)))


print("Ejercicio 2")
from math import sqrt

A = float(input("Escriba el valor del coeficiente a: "))
B = float(input("Escriba el valor del coeficiente b: "))
C = float(input("Escriba el valor del coeficiente c: "))
x1= 0
x2= 0

dis= ((B**2)-4*A*C)

if dis < 0:
  print("Ecuación no presenta solución real.")
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)