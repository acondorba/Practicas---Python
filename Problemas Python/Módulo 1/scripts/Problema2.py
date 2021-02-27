print ("Problema 2")
#Ingresar el dato
dato = input("¿Cuál es tu texto?")

if dato==dato.upper(): #para mayusculas
    abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
else:
    abc="abcdefghijklmnñopqrstuvwxyz" #para minusculas
    
key=int(input("Ingresar valor de desplazamiento"))

cifrado=""

#cifrado
for caracter in dato:
    if caracter in abc:
        cifrado += abc[(abc.index(caracter)+key)%(len(abc))]
    else:
        cifrado+=caracter
            

print ("Texto cifrado:",cifrado)