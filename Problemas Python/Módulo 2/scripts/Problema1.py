print("Problema Mario Bros")
numero = int(input("Escriba un número positivo entre 1 y 8: "))
while numero<=0 or numero>=9:
    print("¡Ha escrito un fuera del rango! Inténtelo de nuevo")
    numero = int(input("Escriba un número positivo: "))
for i in range(1,numero+1):
        print (" " * (numero-i) + "#" * i)