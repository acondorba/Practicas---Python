def cantidad():
    n=int(input("Ingrese cantidad de alumnos:"))
    print (n)
    return n

def nota():
    nota = float(input("Introduce la nota(0 - 10): "))
    return nota

def validar_nota(nota):
    try:
        c=nota()
        #nota = float(input("Introduce la nota(0 - 10): "))
        if c >=0 and c <= 10:
            return c  # Importante romper la iteración si todo ha salido bien
        else:
            print('Nota fuera del rango')
            print("Ingrese nota nuevamente:")
            na = float(input("Introduce la nota(0 - 10): "))
            return na

    except:
        print("Ha ocurrido un error, introduce bien la nota")
        
def ingresar_alumnos(n):
    promedio=0
    aprobados=0
    desaprobados=0
    total = 0
    lista_alumnos = []
    lista =[]
    for i in range (n):
        alumno ={}
        nom = input("Ingrese el nombre del alumno {}:".format(i+1))
        alumno['Nombre']=nom
        alumno['Nota1']=validar_nota(nota)
        alumno['Nota2']=validar_nota(nota)
        alumno['Nota3']=validar_nota(nota)
        alumno['Prom']=round(((alumno['Nota1']+alumno['Nota2']+alumno['Nota3'])/3),2)
        promedio = alumno['Prom']
        dato = nom + " " + str(promedio)
        if promedio>=4:
            alumno['Estado']="Aprobado"
            aprobados+=1
            total+=promedio
        else:
            alumno['Estado']="Desaprobado"
            desaprobados+=1
            total+=promedio
            # agregando alumno a lista alumnos
        lista_alumnos.append(alumno)
        lista.append(dato)
    print ("---------------------------------------------------------------------------------------------------------------------------------")
    print(lista_alumnos)
#    print ("Promedio más alto y promedio más bajo",lista)
#    return (aprobados,desaprobados,total,n,lista_alumnos,maxi,mini)

    maxi=lista[0]
    mini=lista[0]
    
    for valor in lista:
        if lista[i]>=maxi:
                maxi=lista[i]
        elif lista[i]<=mini:
                mini=lista[i]
#    return maxi,mini
    print ("---------------------------------------------------------------------------------------------------------------------------------")
    print('A continuación se lista la mayor y menor nota:')
    print(maxi)
    print(mini)
    return (aprobados,desaprobados,total,n,lista_alumnos)
    
def imprimir(x,y,z,n,a):
    prom_cur=round(float(z/n),2)
    print ("---------------------------------------------------------------------------------------------------------------------------------")
    print ("La cantidad de aprobados son: {} \nLa cantidad de desaprobados son: {} \nEl promedio total del curso es: {} ".format(x,y,prom_cur))
    print ("---------------------------------------------------------------------------------------------------------------------------------")
    return (a)


#def buscar(a):
    #print(type(a))
    #a=str(input("Ingrese palabra a buscar:"))
    #x = dict(a)
    #x.get(a)

n=cantidad()
#lista_alumnos=ingresar_alumnos(n)
aprobados,desaprobados,total,n,a=ingresar_alumnos(n)
#validar_promedio(lista_alumnos)
imprimir(aprobados,desaprobados,total,n,a)
#buscar(a)
